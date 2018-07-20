from socket import *



Sscoket = socket(AF_INET, SOCK_STREAM)


Sscoket.bind(('', 8090))

Sscoket.listen(50)

conn, addr = Sscoket.accept()

recvData = conn.recv(1024)
print(recvData)
if recvData:
    conn.send(b'123')

