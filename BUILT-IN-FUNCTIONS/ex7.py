def extract_full_name(name_list):
	# first_names = list(map(lambda x: x['first'], name_list))
	# print(first_names)
	# last_names = list(map(lambda x: x['last'], name_list))
	# print(last_names)
	# return [' '.join(x) for x in list(zip(first_names, last_names))]

	# return list(map(lambda x: (x['first'] + ' ' + x['last']), name_list))
	# return list(map(lambda x: '{} {}'.format(x['first'],x['last']), name_list))
	return list(map(lambda x: f"{x['first']} {x['last']}", name_list))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

print(extract_full_name(names))