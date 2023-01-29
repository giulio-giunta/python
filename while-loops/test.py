from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

# while number != 5:
# 	number = randint(1,10)
# 	print(f'Your number is {number}')
# 	i += 1
# 	print(f'You had to iterated {i} times to get {number}')

while number != 5:
	number = randint(1,10)
	print('Your number is {}'.format(number))
	i += 1
	print('You had to iterated {} times to get {}'.format(i, number))