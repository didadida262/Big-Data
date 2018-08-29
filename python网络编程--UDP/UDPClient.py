from socket import *

severName = '192.168.0.104'
severPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = raw_input('Input a sentence:')
clientSocket.sendto(message,(severName,severPort))
modifiedMessage,severAddress = clientSocket.resvfrom(2048)
print modifiedMessage
clientSocket.close()