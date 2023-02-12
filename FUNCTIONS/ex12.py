'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(word):
	return {k: word.count(k) for k in word}
	
print(multiple_letter_count('annalisa'))