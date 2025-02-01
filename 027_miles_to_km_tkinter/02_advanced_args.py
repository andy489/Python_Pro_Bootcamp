def my_func1(a=1, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")


# my_func1(100)
# my_func1(b=100)

def my_func2(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")


my_func2(100)
# my_func2(b=100) # boom
my_func2(1, b=100)
