def count_up_to(max):
	count = 1
	while count < max:
		yield count
		count += 1

counter = count_up_to(5)
print(next(counter))
print('any word')

for num in counter:
	print(num)