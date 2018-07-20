import gevent
from gevent import monkey
monkey.patch_all()
import requests


def test():
    print(gevent.getcurrent())
    r = requests.get('http://127.0.0.1:8000/api/test')
    print(r.status_code)

gevent.joinall([
        gevent.spawn(test),
        gevent.spawn(test),
        gevent.spawn(test),
        gevent.spawn(test)
    ])


#
#
# from gevent import monkey; monkey.patch_all()
# import gevent,requests
# import time
#
# def f():
#     print(1)
#     data = requests.get('http://127.0.0.1:8000/api/test')
#     print(data)
#
# start = time.time()
# url_list = []
# for i in range(5):
#     url_list.append(gevent.spawn(f))
#
# gevent.joinall(url_list)
# print(time.time() - start)
#
#

