from flask import Flask
from random import randint

from html_decorators import *

app = Flask(__name__)


@app.route("/")
def index():
    return ('<h1 style="text-align: center">Hello, Flask!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://d2zp5xs5cp8zlg.cloudfront.net/image-61785-800.jpg" width=320/>'
            '<img src="https://www.vets4pets.com/siteassets/species/cat/kitten/tiny-kitten-in-field.jpg?width=1040" width=378/>'
            '<br>'
            '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200/>')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/greet")
def greet_user(name: str):
    return f"Hello, {name.capitalize()}"


@app.route("/random/<int:upto>")
def rand_upto(upto: int):
    return f"Your random positive integer number up to {upto} is: {randint(0, upto)}"


if __name__ == "__main__":
    app.run(debug=True)
