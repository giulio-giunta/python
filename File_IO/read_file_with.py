with open('test.txt') as f:
	data = f.read()

print(f.closed)
# print(f.read())
print(data)
print(f.closed)