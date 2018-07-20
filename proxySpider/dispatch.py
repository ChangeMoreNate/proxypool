from proxygetter import proxy_66ip
from testproxy import TestProxyAndHandle
from multiprocessing import Process
from config.conf import NUM




getP = proxy_66ip()
testP = TestProxyAndHandle()

def app():
    p1 = Process(target=getP.run)
    p2 = Process(target=testP.run, args=(NUM,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    app()


