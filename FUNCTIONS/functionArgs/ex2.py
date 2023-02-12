def combine_words(word, **kwargs):

	# for k,v in kwargs.items():
	# 	if k == 'prefix':
	# 		return v + word
	# 	elif k == 'suffix':
	# 		return word + v
	# 	return word

	if 'prefix' in kwargs:
		return kwargs['prefix'] + word
	elif 'suffix' in kwargs:
		return word + kwargs['suffix']
	return word
print(combine_words('work', suffix='er'))






combine_words("child")  #'child'

combine_words("child", prefix="man")  #'manchild'

combine_words("child", suffix="ish")  #'childish'

combine_words("work", suffix="er")  #'worker'

combine_words("work", prefix="home")  #'homework'