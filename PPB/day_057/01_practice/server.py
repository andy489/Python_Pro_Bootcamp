from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html",
                           num=random_number,
                           year=current_year,
                           )


@app.route("/guess/<name>")
def guess(name: str):
    predicted_age = requests.get(f"https://api.agify.io/?name={name}")
    predicted_age.raise_for_status()

    predicted_gender = requests.get(f"https://api.genderize.io/?name={name}")
    predicted_gender.raise_for_status()

    age_data = predicted_age.json()
    gender_data = predicted_gender.json()

    return render_template("guess.html",
                           name=name.capitalize(),
                           age=age_data["age"],
                           gender=gender_data["gender"],
                           )


@app.route("/blog/", defaults={"num": None})
@app.route("/blog/<num>")
def get_blog(num):
    if num:
        print(num)

    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
