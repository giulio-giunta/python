# def speak(animal='dog'):
# 	if animal == 'pig':
# 		return 'oink'
# 	elif animal == 'duck':
# 		return 'quack'
# 	elif animal == 'cat':
# 		return 'meow'
# 	elif animal == 'dog':
# 		return 'woof'
# 	return '?'

# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"

def speak(animal='dog'):
    '''
    >>> speak('pig')
    'oink'
    '''
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')


print(speak())
print(speak('duck'))
print(speak('cat'))
print(speak('elephant'))