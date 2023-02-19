from termcolor import colored

# dir(termcolor)
# help(termcolor)

text = colored('HI THERE!', color='red', on_color='on_cyan', attrs=['bold'])
print(text)
