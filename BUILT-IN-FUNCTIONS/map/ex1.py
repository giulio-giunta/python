# def decrement_list(my_list):
# 	return [(i-1) for i in my_list]

# print(decrement_list([1,2,3]))

def decrement_list(my_list):
	return list(map(lambda x: x-1, my_list))
	 
print(decrement_list([1,2,3]))


