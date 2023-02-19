import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format('DAD JOKE 3000')
header = colored(header, color='magenta')
print(header)

url = 'https://icanhazdadjoke.com/search'
user_input = input('Let me tell you a joke! Give ve a topic: ')

response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={
        'term': user_input
    }
).json()

num_jokes = response['total_jokes']
if num_jokes != 0:
    print(f'I found {num_jokes} jokes related to {user_input}: here is one!')
    print(response['results'][choice(range(num_jokes))]['joke'])
else:
    print(f'Sorry, I don\'t have any jokes about {user_input}')
