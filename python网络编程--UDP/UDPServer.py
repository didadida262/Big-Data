from socket import *
socketPort = 12000
serverSocket =socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',socketPort))
print "serverSocket is ready to receive:"

while True:
	message,clientAddress = serverSocket.recvfrom(2048)
	print message
	modifiedMessage = message.upper()

	serverSocket.sendto(modifiedMessage,clientAddress)