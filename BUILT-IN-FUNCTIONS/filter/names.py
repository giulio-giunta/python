names = ['austin', 'penny', 'anthony', 'angel', 'billy']
a_names = list(filter(lambda name: name[0].lower() == 'a', names))

print(a_names)