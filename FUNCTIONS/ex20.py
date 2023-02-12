'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(num):
    return num % 2 == 0

# def partition(my_list, fn):
#     truthy = []
#     falsy = []
#     for i in my_list:
#         if fn(i):
#             truthy.append(i)
#         else:
#             falsy.append(i)
#     return [truthy, falsy]

def partition(my_list, fn):
    return [[i for i in my_list if fn(i)], [i for i in my_list if not fn(i)]]

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]