from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    # https://jinja.palletsprojects.com/en/stable/
    # https://updateyourfooter.com/

    rand_num = random.randint(1, 100)
    curr_year = datetime.datetime.now().year

    return render_template("home.html",
                           num=rand_num, year=curr_year)


@app.route("/guess/<string:name>")
def guess(name):
    # https://agify.io/documentation
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(url=age_url)
    age_response.raise_for_status()
    age_data = age_response.json()

    # https://genderize.io/documentation
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(url=gender_url)
    gender_response.raise_for_status()
    gender_data = gender_response.json()

    return render_template("guess.html",
                           name=name,
                           gender=gender_data["gender"],
                           age=age_data["age"])


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    # https://www.npoint.io/
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
