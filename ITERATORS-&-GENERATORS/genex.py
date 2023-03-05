# def nums():
# 	for num in range(1,5):
# 		yield num

# g = nums()

g = (num for num in range(1,5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))