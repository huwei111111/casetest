import threading

"""
并发的线程，多个线程并发触发
"""


def ss():
    print('I am testing code!')


def thd():
    s = []
    for i in range(10):
        t = threading.Thread(target=ss)
        s.append(t)
    for t in s:
        t.start()


thd()
