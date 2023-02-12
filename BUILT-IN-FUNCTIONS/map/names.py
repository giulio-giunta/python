names = [
	{'first': 'Rusty', 'last': 'Steele'},
	{'first': 'Colt', 'last': 'Steele'},
	{'first': 'Blue', 'last': 'Steele'},
]

# first_names = map(lambda name: name['first'], names)
# first_names = list(first_names)
first_names = list(map(lambda name: name['first'], names))

print(first_names)