from random import random

# def flip_coin():
# 	# generate random number from 0 to 1
# 	r = random()
# 	if r > 0.5:
# 		return 'Heads'
# 	else:
# 		return 'Tails'

def flip_coin():
	if random() > 0.5:
		return 'HEADS'
	else:
		return 'TAILS'
print(flip_coin())


