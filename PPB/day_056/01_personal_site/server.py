from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cv():
    return render_template("cv.html")


@app.route("/card")
def name_card():
    return render_template("name-card.html")

if __name__ == "__main__":
    app.run(debug=True)
