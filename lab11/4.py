import urllib.request
import time
import threading as trd


urls_list = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
]


def parse_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
threads_list = [
    trd.Thread(target=parse_url, args=(url,)) for url in urls_list
]
for thread in threads_list:
    thread.start()
for thread in threads_list:
    thread.join()
print(time.time() - start)
"""
LMAO, sample code dropped with URLError, so I had to remove one url to run it and count time
time without threading - ~1.55s
time with threading - ~0.71s
"""