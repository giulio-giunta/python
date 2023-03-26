'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(file_ori, file_copy):
    with open(file_ori) as file_ori:
        content = file_ori.read()
    with open(file_copy, 'w') as file_copy:
        file_copy.write(content)

print(copy('story.txt', 'story_copy.txt'))