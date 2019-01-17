from socket import *

HOST = '10.164.14.216'
PORT = 6789
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(1)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()

    try:
        data = tcpCliSock.recv(BUFSIZE)
        #print(data)                    #data是一个get的http请求报文
        filename = data.split()[1]      #filename = /HelloWorld.html
        #print(filename[1:])
        f = open(filename[1:])          #f = HelloWorld.html    
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\r\n\r\n'       #回复报文
        tcpCliSock.send(header.encode())
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        tcpCliSock.close()
    except IOError:
        header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        tcpCliSock.send(header.encode())
        tcpCliSock.close()
tcpSerSock.close()
