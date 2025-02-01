def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# * accepts any number of arguments, treats iterable data as positional arguments
print(add(1, 3, 5))
print(add(*[1, 3, 5, 7]))
print(add(*(1, 3, 5, 7, 9)))
print(add(*{1, 3, 5, 7, 9, 11}))
