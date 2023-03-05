# Find prime numbers between 1 and 20

# range_numbers = set(range(1,100))
# prime = []
# non_prime = []

# for i in range_numbers:
# 	for num in range_numbers:
# 		if (i % num == 0):
# 			if num == 1 or num == i:
# 				pass
# 			else:
# 				non_prime.append(i)
				
# prime = range_numbers - set(non_prime)
# print(prime)

def prime_numbers(end, start=1):
	non_prime = []
	for i in range(start,end):
		for num in range(start,end):
			if (i % num == 0):
				if num == 1 or num == i:
					pass
				else:
					non_prime.append(i)
					
	prime = list(set(range(start,end)) - set(non_prime))
	return sorted(prime)

print(prime_numbers(10000))