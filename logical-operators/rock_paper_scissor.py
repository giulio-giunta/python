print('...rock...')
print('...paper...')
print('...scissor...')

player1 = input('Enter Player 1\'s choice ')
print(20*'\n NO CHEATING')
player2 = input('Enter Player 2\'s choice ')

while (player1 != 'exit') or (player2 != 'exit'):
	if player1 == 'exit':
		print('Player 1 doesn\'t want to play anymore')
		break
	elif player2 == 'exit':
		print('Player 2 doesn\'t want to play anymore')
		break

	wrong_value1 = (player1 != 'rock' and player1 != 'paper' and player1 != 'scissor')
	wrong_value2 = (player2 != 'rock' and player2 != 'paper' and player2 != 'scissor')

	if wrong_value1 and wrong_value2:
		print('You both inserted wrong values')
	elif wrong_value1:
		print('Player 1 inserted a wrong value')
	elif wrong_value2:
		print('Player 2 inserted a wrong value')
	elif player1 == player2:
		print('It\'s a draw!') 
	elif player1 == 'rock' and player2 == 'scissor':
		print('Player 1 wins')
	elif player1 == 'paper' and player2 == 'rock':
		print('Player 1 wins')
	elif player1 == 'scissor' and player2 == 'paper':
		print('Player 1 wins')
	else: 
		print('Player 2 wins')

	player1 = input('Enter Player 1\'s choice ')
	print(20*'\n NO CHEATING')
	player2 = input('Enter Player 2\'s choice ')
	
	
	