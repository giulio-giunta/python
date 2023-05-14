# BAD!
# with open('frows.csv') as file:reader
# 	data = file.read()
# print(data)

# Using reader
# from csv import reader
# with open('frows.csv') as file:
# 	csv_reader = reader(file)
# 	next(csv_reader)
# 	for frow in csv_reader:
# 		print(f'{frow[0]} is from {frow[1]}')

# from csv import reader
# with open('frows.csv') as file:
# 	csv_reader = reader(file)
# 	data = list(csv_reader)
# 	print(data)

# Using reader
# from csv import DictReader
# with open('fighters.csv') as file:
# 	csv_reader = DictReader(file)
# 	for row in csv_reader:
# 		print(row['Name'])
		
# Using reader
from csv import DictReader
with open('fighters2.csv') as file:
	csv_reader = DictReader(file, delimiter='|')
	for row in csv_reader:
		print(row['Name'])