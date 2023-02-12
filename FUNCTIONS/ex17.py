'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(my_string):
	# return my_string.capitalize()
	return my_string[0].upper() + my_string[1:]
print(capitalize('giulio'))