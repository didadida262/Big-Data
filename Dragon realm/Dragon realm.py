import time
import random

def BeginGame():
	print('You are in a land full of drangons.In front of you,')
	print()
	time.sleep(2)
	print('you can see two caves.in one cave,the dragon is friendly')
	print()
	time.sleep(3)
	print('and will share his treasure with you.')
	print('but the other is greedy and hungry')
	print()
	time.sleep(3)
	print('and will eat you on sight')
	print()

def CaveChoose():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into?(1 or 2)')
		cave = input()
		return cave

def CheckCave(cave):
	print('You approach the cave...')
	print()
	print('It is dark...')
	time.sleep(2)
	print('A large drangon jumps out in front of you!')
	time.sleep(3)
	print('he opens his jaws and..')
	time.sleep(4)
	friendlycave = random.randint(1,2)
	if cave == str(friendlycave):
		print('Give you his treasure')
	else:
		print('Gabbles you down in one bite')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	BeginGame()
	cavenum = CaveChoose()
	CheckCave(cavenum)

	print('Do you want to play again?(yes or no)')
	playAgain = input ()
