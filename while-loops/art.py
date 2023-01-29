emoji = '\U0001f600'
num_emoji = 1
num_empty_space = 20
empty_space = ' '

while num_emoji <= 20:
	print(num_empty_space * empty_space + num_emoji * emoji)
	num_empty_space -= 2
	num_emoji += 2
