from socket import *
from datetime import *
from time import *

host ='127.0.0.1'
port = 1234
ADDR = (host,port)
udpClisocket = socket(AF_INET,SOCK_DGRAM)
TIMEOUT = 1
udpClisocket.settimeout(TIMEOUT)
BUFSIZE = 1024

for i in range(0,10):
	data = input('> ')
	if not data:
		break
	try:
		begin_time = datetime.now()
		udpClisocket.sendto(data.encode(),ADDR)
		data,addr = udpClisocket.recvfrom(BUFSIZE)
		end_time = datetime.now()
		print('Response: ',data)
		time = (end_time - begin_time).microseconds
		print('RTT: ',time,'ms')

	except Exception as e:
		print(e)
udpClisocket.close()
