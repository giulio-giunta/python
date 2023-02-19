from pyfiglet import figlet_format
from termcolor import colored


def print_art(msg, color):
    valid_colors = (
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
        'light_grey',
        'dark_grey',
        'light_red',
        'light_green',
        'light_yellow',
        'light_blue',
        'light_magenta',
        'light_cyan')
    if color not in valid_colors:
        color = 'blue'
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    return colored_ascii


msg = input('What would you like to print? ')
color = input('What color? ')

print(print_art(msg, color))
