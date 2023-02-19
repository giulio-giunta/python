class Pet():
	allowed = ['cat', 'dog', 'fish', 'rat']
	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f'You can\'t have a {species} pet')
		self.name = name
		self.species = species
	def set_species(self, species):
		if species not in Pet.allowed:
			raise ValueError(f'You can\'t have a {species} pet')
		self.species = species

cat = Pet('Blue', 'cat')
dog = Pet('Wyatt', 'dog')

print(cat.species)
print(dog.species)

cat.set_species('rat')
print(cat.species)

# Pet.allowed.append('pig')
# print(Pet.allowed)
# dog.species = 'pig'
# print(dog.species)

print(cat)
print(dog)

print(id(cat.allowed)) # Refers to the same location in memory
print(id(dog.allowed)) # Refers to the same location in memory
print(id(Pet.allowed)) # Refers to the same location in memory
