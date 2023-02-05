string = 'hello julian'

print({char for char in string if char in 'aeiou'})


def are_all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiou' })
result = are_all_vowels_in_string(string)
if result < 5:
	print(f'not all vowels are in the {string} string')
else: 
	print(f'there are all vowels in the {string} string')