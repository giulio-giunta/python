def contains_purple(*args):
	for arg in args:
		if str(arg).lower() == 'purple': return True
	return False

print(contains_purple("Purle", 'main', 0, True, 'hella'))