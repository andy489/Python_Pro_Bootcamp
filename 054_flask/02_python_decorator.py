# Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after

    return wrapper_function

@delay_decorator
def say_hello():
    # time.sleep(2)
    print("Hello")

def say_bye():
    # time.sleep(2)
    print("Bye")

def say_greeting():
    # time.sleep(2)
    print("How are you?")

# delay_decorator(say_hello)()
say_hello()
