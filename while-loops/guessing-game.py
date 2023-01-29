from random import randint

guess = 0
number = randint(1,10)

print(number)

while guess != number:
	guess = input('Guess a number between 1 and 10: ')
	guess = int(guess)
	if guess < number:
		print('Too low, try again!')
	elif guess > number:
		print('Too high, try again!')
	else:
		print('You guessed it! You won!')
		
	
	
	