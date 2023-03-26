'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(file_ori, file_copy):
    with open(file_ori) as file_ori:
        content = file_ori.read()
        new_content = content[::-1]
        with open(file_copy, 'w') as file_copy:
            file_copy.write(new_content)

print(copy_and_reverse('story.txt', 'story_reversed.txt'))