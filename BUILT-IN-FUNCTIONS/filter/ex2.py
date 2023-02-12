def remove_negatives(nums):
	return list(filter(lambda	n: n >= 0, nums))

print(remove_negatives([-1,3,4,-99]))