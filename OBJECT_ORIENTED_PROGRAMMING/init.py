# A Vehicle class with 3 attributes but no methods (aside from __init__)

class Vehicle:

	# def __init__(test, make, model, year):
	# 	test.casa = make
	# 	test.modello = model
	# 	test.anno = year

	def __init__(test, make, model, year):
		test.make = make
		test.model = model
		test.year = year

v1 = Vehicle('Fiat', '127', 1985)
v2 = Vehicle('Lancia', 'Beta', 1974)

# print(v1.casa, v1.modello, v1.anno)

print(v1.make, v1.model, v1.year)
print(v2.make, v2.model, v2.year)