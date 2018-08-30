from socket import *

serverPort = 12000


serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
	connectSocket,clientAdd = serverSocket.accept()
	message = connectSocket.recv(1024)
	print message
	ans = raw_input()
	ans = 'dida263: ' + ans
	connectSocket.send(ans,clientAdd)
	connectSocket.close()