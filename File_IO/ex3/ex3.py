'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(file):
    with open(file) as file:
        lines = file.readlines()
        return {"lines": len(lines),
                "words": sum(len(line.split()) for line in lines),
                'characters': sum(len(line) for line in lines)}
        
print(statistics('story.txt'))
