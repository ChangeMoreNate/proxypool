import gevent
from gevent import monkey
monkey.patch_all()
import requests
from config.conf import URL
from Redisclient import Redis
from ramdom_headers import get_headers
import time
import json





class TestProxyAndHandle(object):

    def __init__(self):
        self.redis = Redis()


    def testrawproxy(self, proxy):
        """
        代理测试器是否可以访问目标网站，如果可以返回，交给代理处理器处理
        :return:
        """
        print(proxy)
        proxies = {
            'https': 'https://' + proxy,
            'http': 'http://' + proxy,
        }
        headers = get_headers()
        try:
            r = requests.get(URL, headers=headers, proxies=proxies, timeout=5)
            print(r.status_code)
            if r:
                ip = json.loads(r.text)['origin'].split(',')
                print(ip)
                if len(ip) < 2:
                    print('proxy: %s 可用' % proxy)
                    self.redis.rpush('goodproxies', proxy)
                else:
                    print('非高匿名')
            else:
                print('proxy: %s 不可用' % proxy)
        except Exception:
            print('proxy: %s 不可用并出现异常' % proxy)


    def testgoodproxy(self, proxy):
        """
        代理测试器是否可以访问目标网站，如果可以返回，交给代理处理器处理
        :return:
        """
        print(proxy)
        proxies = {
            'https': 'https://' + proxy,
            'http': 'http://' + proxy,
        }
        headers = get_headers()
        try:
            r = requests.get(URL, headers=headers, proxies=proxies, timeout=5)
            if r:
                ip = json.loads(r.text)['origin'].split(',')
                print(ip)
                print(len(ip))
                if len(ip) < 2:
                    print('goodproxy: %s 可用' % proxy)
                    self.redis.rpush('goodproxies', proxy)
                else:
                    print('非高匿名')
            else:
                print('goodproxy: %s 不可用' % proxy)
        except Exception:
            print('goodproxy: %s 不可用并出现异常' % proxy)


    def run(self, num):

        while True:
            task_list = []

            if len(self.redis.lrange('goodproxies')) > 5:
                for i in range(num):
                    proxy = self.redis.lpop('goodproxies')
                    print('good', proxy)
                    if proxy != 0:
                        gevent.spawn(self.testgoodproxy, proxy)

            if len(self.redis.lrange('goodproxies')) < 100:
                for i in range(num):
                    proxy = self.redis.lpop('proxies')
                    print('proxy', proxy)
                    if proxy != 0:
                        gevent.spawn(self.testrawproxy, proxy)
            else:
                time.sleep(10)

            gevent.joinall(task_list)
            time.sleep(10)


if __name__ == '__main__':
    t = TestProxyAndHandle()
    t.run(10)