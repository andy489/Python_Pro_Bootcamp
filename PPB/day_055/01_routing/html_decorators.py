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


def wrap(*items):
    """
    Universal decorator that works both ways:
    - @Wrap           (wraps in <b> tags)
    - @Wrap()         (wraps in <b> tags)
    - @Wrap('tag')    (wraps in specified tag)
    - @Wrap('t1','t2') (wraps in multiple tags)
    - @wrap({'class': 'container'}, 'div', {'style': 'color: blue;'}, 'h1', 'u', 'i') (alias and tags with attributes)
    """

    # Build tag-attribute pairs
    tag_attr_pairs = []
    pending_attrs = {}

    for item in items:
        if isinstance(item, dict):
            pending_attrs = item.copy()
        elif isinstance(item, str):
            tag_attr_pairs.append((item, pending_attrs.copy()))
            pending_attrs = {}

    # Default if no tags
    if not tag_attr_pairs:
        tag_attr_pairs = [('b', {})]

    # Create the actual decorator
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for tag, attrs in reversed(tag_attr_pairs):
                if attrs:
                    attrs_str = ' ' + ' '.join(f'{key}="{value}"' for key, value in attrs.items())
                    result = f"<{tag}{attrs_str}>{result}</{tag}>"
                else:
                    result = f"<{tag}>{result}</{tag}>"
            return result

        return wrapper

    # Handle @wrap without parentheses
    if len(items) == 1 and callable(items[0]):
        return decorator(items[0])

    return decorator


# Alias with capital W if you want
Wrap = wrap