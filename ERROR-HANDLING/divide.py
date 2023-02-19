def divide(a,b):
	try:
		result = a/b
	# except (ZeroDivisionError, TypeError) as err:
	# 		print('Something went wrong!')
	except ZeroDivisionError as errore:
		print('don\'t divide by zero, please')
		print(errore)
	except TypeError as err:
		print(' a and b must be ints or floats')
		print(err)
	else:
		print(f'{a} divided by {b} is {result}')
	
print(divide(1,2))
print(divide(1,0))
print(divide(2,'e'))