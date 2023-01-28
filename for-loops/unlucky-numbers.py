# for x in range(1, 21):
# 	if x % 2 != 0 and x != 13:
# 		print(f'{x} is odd')
# 	elif x % 2 == 0 and x != 4:
# 		print(f'{x} is even')
# 	else:
# 		print(f'{x} IS UNLUCKY!')
	
# for x in range(1, 21):
# 	if x == 4 or x == 13:
# 		print(f'{x} IS UNLUCKY!')
# 	elif x % 2 != 0:
# 		print(f'{x} is odd')
# 	else:
# 		print(f'{x} is even')

for x in range(1, 21):
	if x == 4 or x == 13:
		state = 'UNLUCKY!'
	elif x % 2 != 0:
		state = 'odd'
	elif x % 2 == 0:
		state = 'even'
	print(f'{x} is {state}')
		