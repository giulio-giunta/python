'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(my_list):
	if my_list:
		return my_list[-1]
	return None

print(last_element([True, 1, 'my', 'name', 3, 'is']))