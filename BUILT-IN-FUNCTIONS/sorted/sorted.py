# It's a method similar to .sort(), but it accepts tuples along with lists and instead of sorting list 
# values in place, it sorts them in the output. With 'reverse=True', it sorts in the opposite order.

# nums = [4,6,8,34,23,54]
# nums.sort()
# print(nums)

# nums = [4,6,8,7,34,23,54]
# print(sorted(nums))
# print(sorted(nums, reverse=True))
# print(nums)

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], 'a': 3, 'color': 'purple'},
	{"username": "bob123", "tweets": [], 'color': 'red'},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# print(sorted(users,key=len))

# print(sorted(users,key=(lambda user: user['username'])))

# print(sorted(users,key=(lambda user: len(user['tweets']))))

print(sorted(users,key=(lambda user: len(user['tweets'])), reverse=True))