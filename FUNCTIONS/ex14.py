'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
	return string[::-1].lower().replace(' ','') == string.lower().replace(' ','')
	
print(is_palindrome('a man a plan a canal Panama'))