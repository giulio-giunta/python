emoji = '\U0001f600'

# Syntax that requires closing a file
file = open('haiku.txt', 'w')
file.write('Writing files is great\n')
file.write('Here\'s another line of text\n')
file.write('Closing now, goodbye!')
file.close()

# "write" mode overwrites a file is existing or creates a new file if not existing
with open('haiku.txt', 'w') as file:
	file.write('Here\'s one more haiku\n')
	file.write('What about the older one?\n')
	file.write('Let\'s go check it out')

with open('lol.txt', 'w') as file:
	file.write('haha' * 10000)
	
# "append" mode writes to the end of a file by default
with open('haiku.txt', 'a') as file:
	file.write('\n')
	file.write('Here\'s one more haiku\n')
	file.write('What about the older one?\n')
	file.write('Let\'s go check it out')
	
# If no cursor is specified "read+" mode writes to a file by default at the beginning and overwrites
# the content of an existing file. If the file does not exist, "read+" will throw an error.
with open('haiku.txt', 'r+') as file:
	file.write(':)')
	file.seek(10)
	file.write('(:')

