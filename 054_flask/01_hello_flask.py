# https://pypi.org/project/Flask/
# https://flask.palletsprojects.com/en/stable/quickstart/

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
