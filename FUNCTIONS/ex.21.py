def partition(my_list):
    def isEven(num):
        return num % 2 == 0
    return [[i for i in my_list if isEven(i)], [i for i in my_list if not isEven(i)]]


print(partition([0, 1, 2, 3, 4, 7]))