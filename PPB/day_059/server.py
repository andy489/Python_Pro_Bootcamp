from flask import Flask, render_template
import requests
import datetime

posts = requests.get("https://api.npoint.io/2378d3d8e0262f7e23d3").json()

app = Flask(__name__)

curr_year = datetime.datetime.now().year

@app.context_processor
def inject_footer_data():
    return {
        "curr_year": curr_year,
    }


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
