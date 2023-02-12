def display_names(first, second):
	print(f'{first} says hello to {second}')

names = {'first': 'Colt', 'second': 'Rusty'}

display_names(first='Charlie', second='Sue')

display_names(**names)