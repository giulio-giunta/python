def sum_floats(*args):
	return sum(arg for arg in args if type(arg) == float)

print(sum_floats(*[1, 1.5, 2, 2.7]))