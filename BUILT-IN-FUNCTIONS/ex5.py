def interleave(h1, h2):
	z =  zip(h1, h2)
	return ''.join(''.join(list(x)) for x in z)

print(interleave('hi', 'ha'))
