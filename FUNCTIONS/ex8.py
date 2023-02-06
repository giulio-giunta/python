'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# def return_day(num):
# 	for i in range(num):
# 		if 1 <= num <= 7:
# 			return days[num-1]

# 	return None

# print(return_day(8))

# days = {'1':'Sunday', '2': 'Monday', '3': 'Tuesday', '4': 'Wednesday', '5': 'Thursday', '6': 'Friday', '7': 'Saturday'}

# def return_day(num):
# 	for k in days.keys():
# 		if num == int(k):
# 			return days[k]
# 	return None

# print(return_day(3))

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

print(return_day(3))