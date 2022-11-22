import os, re
import threading as trd


received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")


def pinger(ip): #idk how to name this one
    ping = os.popen("ping -q -c2 " + ip, "r") 
    print("... pinging ", ip) # I have no idea about a point of this row but it was in task
    while True:
        line = ping.readline()
        if not line:
            break
        received = received_packages.findall(line)
        if received:
            print(ip + ": " + status[int(received[0])])


threads_list = [
        trd.Thread(target=pinger, args=("192.168.178." + str(suffix),))
        for suffix in range(20, 30)
]
for thread in threads_list:
    thread.start()
for thread in threads_list:
    thread.join()