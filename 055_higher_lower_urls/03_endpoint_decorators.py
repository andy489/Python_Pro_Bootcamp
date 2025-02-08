from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        result = "<b>" + function() + "</b>"
        return result

    return wrapper

def make_emphasis(function):
    def wrapper():
        result = "<i>" + function() + "</i>"
        return result

    return wrapper

def make_underline(function):
    def wrapper():
        result = "<u>" + function() + "</u>"
        return result

    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"

@app.route("/")
def index():
    return ('<h1 style="text-align:center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGk2bGJwMW5xa3YwM3g5NXp6dDIxMjN6dmZjMzI3a2J5N2xlZm5rZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2yLNN4wTy7Zr8JSXHB/giphy.gif"'
            'width=500px/>')

if __name__ == "__main__":
    app.run(debug=True)