import random


def inputPlayerLetter():
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Do you want to be X or O ?')
		letter = input().upper()
	if letter =='X':
		return ['X','O']
	else:
		return ['O','X']

def whoGoesFirst():
	if random.randint(0,1) == 1:
		return 'computer'
	else:
		return 'player'

def drawBoard(board):
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('----------------------------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('----------------------------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def makeMove(board,letter,move):
	board[move] = letter

def isSpaceTree(board,move):
	return board[move] == ' '

def getPlayerMove(board):
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceTree(board,int(move)):
		print('what is your next move(1-9)?')
		move = input()
	return int(move)

def isWinner(bo,le):
	return ((bo[1] == le and bo[2] ==le and bo[3] == le) or
		(bo[4] == le and bo[5] == le and bo[6] == le) or
		(bo[7] == le and bo[8] == le and bo[9] == le) or
		(bo[1] == le and bo[4] == le and bo[7] == le) or
		(bo[2] == le and bo[5] == le and bo[8] == le) or
		(bo[3] == le and bo[6] == le and bo[9] == le) or
		(bo[1] == le and bo[5] == le and bo[9] == le) or
		(bo[3] == le and bo[5] == le and bo[7] == le))

def isBoardFull(board):
	for i in range(1,10):
		if isSpaceTree(board,i):
			return False
	return True

def getBoardCopy(board):
	dup = []
	for i in board:
		dup.append(i)

	return dup

def choseRandomMove(board,movelist):
	possiblelist = []
	for i in movelist:
		if isSpaceTree(board,i):
			possiblelist.append(i)

	if len(possiblelist) != 0:
		return random.choice(possiblelist)
	else:
		return None

def getComputerMove(board,letter):
	if letter == 'X':
		player = 'O'
	else:
		player ='X'

#next move will succed
	for i in range(1,10):
		copy = getBoardCopy(board)
		if isSpaceTree(copy,i):
			makeMove(copy,letter,i)
			if isWinner(copy,letter):
				return i
#next move player will succed,find it and block it
	for i in range(1,10):
		copy = getBoardCopy(board)
		if isSpaceTree(copy,i):
			makeMove(copy,player,i)
			if isWinner(copy,player):
				return i
	move = choseRandomMove(board,[1,3,7,9])
	if move != None:
		return move

	if isSpaceTree(board,5):
		return 5
	return choseRandomMove(board,[2,4,6,8])

def playAgain():
	print('do you want to play again?(yes or no)')
	return input().lower().startswith('y')



print('Welcome to Tic Tac Toe')

while True:
	theBoard = [' '] * 10
	playerletter,computerletter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('THE ' + turn + 'will go first')
	gameisplaying = True

	while gameisplaying:
		if turn == 'player':
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard,playerletter,move)
			if isWinner(theBoard,playerletter):
				drawBoard(theBoard)
				print('Congratulation.you have won the game!')
				gameisplaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('the game is a tie')
					break
				else:
					turn = 'computer'
		else:
			move = getComputerMove(theBoard,computerletter)
			makeMove(theBoard,computerletter,move)
			if isWinner(theBoard,computerletter):
				drawBoard(theBoard)
				print('computer win,you have lost')
				gameisplaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('game is a tie')
					break
				else:
					turn = 'player'
	if not playAgain():
			break
