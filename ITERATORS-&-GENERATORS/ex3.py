'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

# def make_song(count=99, beverage='soda'):
#     for i in range(count, -1, -1):
#         if i > 1: yield f'{i} bottles of {beverage} on the wall.'
#         elif i == 1: yield f'Only {i} bottle of {beverage} left'
#         else: yield f'No more {beverage}'

def make_song(count=99, beverage='soda'):
    for x in reversed(range(0,count+1)):
        if x >= 2: yield '{} bottles of {} on the wall.'.format(x,beverage)
        elif x == 1: yield 'Only {} bottle of {} left!'.format(x,beverage)
    yield 'No more {}!'.format(beverage)

default_song = make_song(5,'kombucha')

print(next(default_song)) # '99 bottles of soda on the wall.'
print(next(default_song)) # '99 bottles of soda on the wall.'
print(next(default_song)) # '99 bottles of soda on the wall.'
print(next(default_song)) # '99 bottles of soda on the wall.'
print(next(default_song)) # '99 bottles of soda on the wall.'
print(next(default_song)) # '99 bottles of soda on the wall.'
print(next(default_song)) # '99 bottles of soda on the wall.'
