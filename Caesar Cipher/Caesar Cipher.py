


def GetMode():
	while True:
		print('Do you want to encrypt or decrypt a message?')
		mode = input()
		mode = mode.lower()

		if mode in 'encrypt e decrypt d'.split():
			return mode
		else:
			print('please enter either e or encrypt or d or decrypt')


def GetMessage():
	print('please enter a message:')
	return input()

def GetKey():
	while True:
		print('Enter the key number:')
		key = int(input())
		if (key >=0 and key <= 26):
			return key
		else:
			print('enter a number between 0 and 26')

def GettranMessage(mode,key,message):
	translated = ''
	if mode[0] == 'd':
		key = -key
	for simple in message:
		if simple.isalpha():
			
			num = ord(simple)
			num = num + key
			if simple.isupper():
				if num > ord('Z'):
					num = num - 26
				elif num < ord('A'):
					num = num + 26

			elif simple.islower():
				if num > ord('z'):
					num = num - 26
				elif num < ord('a'):
					num = num + 26
			translated = translated + chr(num)

		else:
			translated = translated + simple


	return translated


mode = GetMode()
message = GetMessage()
key = GetKey()
print('Your translated message is:')

print(GettranMessage(mode,key,message))
