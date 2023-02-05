instructor = dict(name='colt', city='san francisco', color='purple')

yelling_instructor = {(k.upper() if k is 'color' else k): v for k,v in instructor.items()}
print(yelling_instructor)