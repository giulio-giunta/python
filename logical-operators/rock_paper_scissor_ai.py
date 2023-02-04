from random import choice
player = input('Choose rock, paper or scissor ').lower()
computer = choice(['rock', 'paper', 'scissor'])

while player != 'exit':
	print(player)
	print(computer)

	if (player == 'rock' or player == 'paper' or player == 'scissor'):
		if player == computer:
			print('It\'s a draw!') 
		elif player == 'rock' and computer == 'scissor':
			print('Player wins')
		elif player == 'paper' and computer == 'rock':
			print('Player wins')
		elif player == 'scissor' and computer == 'paper':
			print('Player wins')
		else: 
			print('Computer wins')
	else:
		print('Player inserted a wrong value')
	player = input('Choose rock, paper or scissor ').lower()
	computer = choice(['rock', 'paper', 'scissor'])
	
