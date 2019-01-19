from socket import *
import random 

host = ''
port = 1234
ADDR = (host,port)
severSocket = socket(AF_INET,SOCK_DGRAM)
severSocket.bind(ADDR)
BUFSIZE = 1024

while True:
	print('waiting for request...')
	message,addr = severSocket.recvfrom(BUFSIZE)
	message = message.upper()
	rand = random.randint(0,10)
	print(rand,addr)
	if rand < 4:
		continue
	severSocket.sendto(message,addr)
