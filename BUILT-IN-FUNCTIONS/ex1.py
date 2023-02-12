# Implement your is_all_strings function below:
def is_all_strings(my_list):
	return all(type(x) == str for x in my_list)

print(is_all_strings(['a', 'b', 'c', 0]))