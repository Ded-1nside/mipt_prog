import time
import threading as trd


def thread_job(i, lst):
    with lock:
        global total
        total += sum(lst)


def run_threads(num):
    cuts = num
    if num >= len(lst):
        cuts = len(lst)
    threads = [
        trd.Thread(target=thread_job, args=(i, lst[i * cuts:(i + 1) * cuts]))
        for i in range(num)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


lst = [25, 54, 95, 11, 8, 2, 90, 67, 33, 50, 21]
total = 0
num = 9
start = time.time()
lock = trd.Lock()
run_threads(num)
print(time.time() - start)
print(total)

"""
5 threads = ~0.007s
7 threads = ~0.009s
9 threads = ~0.011s
Increasing number of threads decreases speed??? (because of GIL?)
"""