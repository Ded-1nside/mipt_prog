# multiconn-server.py

import sys
import socket
import selectors
from time import time
import types

sel = selectors.DefaultSelector()
users = {}
ENCODING = 'ascii'
MSG_DELIMITER = b'<' #to separate msgs

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(familiar=False, name=b"", msg=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            if not data.familiar:
                name = recv_data.decode(ENCODING)
                users[name] = key
                data.name = name
                data.familiar = True
            else:
                if recv_data == b'list':
                    data.msg = "Online" + ','.join(users.keys()).encode(ENCODING) + "users"
                elif MSG_DELIMITER in recv_data:
                    reciever, msg = recv_data.split(MSG_DELIMITER, 1)
                    reciever = reciever.decode(ENCODING)
                    if reciever in users:
                        users[reciever].data.msg = data.name.encode(ENCODING) + b': ' + msg
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.msg:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]         


try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
    