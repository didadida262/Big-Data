from socket import *

serverName = '192.168.0.104'
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print '开始吧...'
while True:
	message = raw_input()
	message = 'dida262' + message
	clientSocket.send(message)
	modifyMessage = clientSocket.recv(1024)
	print modifyMessage
	clientSocket.close()