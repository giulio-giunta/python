def triple_and_filter(my_list):
	# return [x * 3 for x in my_list if x % 4 == 0]

	# return [x * 3 for x in list(filter(lambda arg: (arg % 4 == 0), my_list))]
	return list(filter(lambda arg: (arg % 4 == 0), map(lambda x: x * 3, my_list)))

print(triple_and_filter([6,8,10,12]))
