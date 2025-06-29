from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# export FLASK_APP=hello_flask.py
# flask run

if __name__ == "__main__":
    app.run()
