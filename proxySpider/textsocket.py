from socket import *


def connSocket(ip, port):
    Csocket = socket(AF_INET, SOCK_STREAM)
    Csocket.connect((ip, port))
    requesthead = """GET / HTTP/1.1\r\nHost: www.taobao.com\r\n\r\n"""
    Csocket.send(requesthead.encode('utf-8'))
    recvData = Csocket.recv(1024)
    print(recvData)





if __name__ == '__main__':

    connSocket('42.123.96.63', 80)
