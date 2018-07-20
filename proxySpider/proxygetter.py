import requests
from Redisclient import Redis
from ramdom_headers import get_headers
import random
from lxml import etree
import time



class proxy_xici(object):
    pass


class proxy_kuaidaili(object):
    pass



class proxy_ip3366(object):
    """
    http://www.ip3366.net/free/?page=2
    """
    pass



class proxy_66ip(object):

    def __init__(self):
        self.redis = Redis()


    def getpage(self, page):

        num = random.randint(2, 18)
        headers = get_headers()
        r = requests.get('http://www.66ip.cn/areaindex_' + str(num) + '/' + str(page) + '.html', headers=headers)
        html = r.content.decode('GBK')
        return html


    def parsepage(self, html):
        num = 0
        h = etree.HTML(html)
        contents = h.xpath('//div[@class="footer"]/div/table[@bordercolor="#6699ff"]/tr')
        try:
            for content in contents:
                ip = content.xpath('./td[1]')[0].text
                port = content.xpath('./td[2]')[0].text
                proxy = ip + ':' + port
                # print(proxy)
                if ip[0] == 'i':
                    continue
                if proxy.encode('utf-8') in self.redis.lrange('proxies'):
                    continue
                num += 1
                self.redis.lpush('proxies', proxy)
            print('------插入', num, '个不相同的代理------')
        except TypeError:
            print('------出现异常------')


    def run(self):

        while True:
            if len(self.redis.lrange('goodproxies')) < 50:
                page = random.randint(1, 10)
                html = self.getpage(page)
                self.parsepage(html)
                time.sleep(10)
            else:
                print('------数量超过50------')
                time.sleep(10)


if __name__ == '__main__':
    p1 = proxy_66ip()
    p1.run()


