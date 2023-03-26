'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file, old_string, new_string):
    with open(file, 'r+') as file:
        content = file.read()
        file.seek(0)
        file.write(content.replace(old_string, new_string))
        file.truncate()
        
print(find_and_replace('story.txt', 'Alice', 'Colt'))