import random


class NoConnection(Exception):
    pass


def connect_user(auth_f):
    with open(auth_f, "w", encoding="utf-8") as f:
        corout = write_to_file(f)
        yield from corout


def write_to_file(f_obj):
    while True:
        try:
            txt = yield
            f_obj.write(txt)
        except NoConnection:
            f_obj.close()
            break

def user_connection(username):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"


def establish_connection(auth=True):
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"


def connection():
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]
