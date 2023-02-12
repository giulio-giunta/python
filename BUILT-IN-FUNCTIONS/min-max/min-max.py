names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(min(len(name) for name in names)) # Tim has 3 character

print(max(name for name in names)) # Tim is the name in the list starting with the max alphabet letter

print(max(names, key=lambda name: len(name))) # Ollivander is the longest name in the list

print(min(names, key=lambda name: len(name))) # Tim is the shortest name in the list
