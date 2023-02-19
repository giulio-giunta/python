from keyword import iskeyword


def contains_keyword(*args):
    for arg in args:
        if iskeyword(arg):
            return True
    return False


print(contains_keyword("hello", "goodbye"))
