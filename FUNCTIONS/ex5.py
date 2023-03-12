def count_dollar_signs(word):
    '''
    >>> count_dollar_signs('how many $$$ do you have?')
    3
    '''
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

print(count_dollar_signs('how many $$$ do you have?'))