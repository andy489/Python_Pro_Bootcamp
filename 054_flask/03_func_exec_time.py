import time
from functools import wraps

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

"""
It's important to add the functools.wraps decorator to preserve the original function name and docstring. 
For example if we take @wraps out of timeit timeit.__name__ would return wrapper and 
timeit.__doc__ would be empty (lost docstring).docstring
"""

def speed_calc_decorator(function):
    """Decorator to tima a function"""
    @wraps(function)
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        print(end - start)

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i