from functools import wraps


def make_bold(func):
    """Decorator that bolds the returned string of a function (wraps it in a <b> html tag)"""

    @wraps(func)
    def wrapper():
        result = "<b>" + func() + "</b>"
        return result

    return wrapper


def make_emphasis(func):
    """Decorator that emphasises the returned string of a function (wraps it in an <em> html tag)"""

    @wraps(func)
    def wrapper():
        result = "<i>" + func() + "</i>"
        return result

    return wrapper


def make_underlined(func):
    """Decorator that underlines the returned string of a function (wraps it in an <u> html tag)"""

    @wraps(func)
    def wrapper():
        result = "<u>" + func() + "</u>"
        return result

    return wrapper
