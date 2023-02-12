'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(my_list):
	product = 1
	total = 0
	even_numbers = [i for i in my_list if i % 2 == 0]
	for x in even_numbers:
		if len(even_numbers) == 0:
			total = 0
		else:
			product = product * x
			total = product
	return total

print(multiply_even_numbers([1, 3, 4, 5, 2, 11]))