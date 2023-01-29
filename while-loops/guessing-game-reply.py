from random import randint

number = randint(1,10)

while True:
	guess = input('Guess a number between 1 and 10: ')
	guess = int(guess)
	if guess < number:
		print('Too low, try again!')
	elif guess > number:
		print('Too high, try again!')
	else:
		print('You guessed it! You won!')
		replay = input('Do you want to keep playing? y/n ')
		if replay == 'y':
			number = randint(1,10)
			guess = 0
		else:
			print('Thank you for playing! Bye!')
			break

	
	

			

			

			
		
		
		