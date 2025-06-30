from flask import Flask, render_template
from post import Post
import requests
from datetime import datetime

POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(POSTS_URL).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

YEAR = datetime.now().year
AUTHOR = "andy489"

app = Flask(__name__)


@app.context_processor
def inject_footer_data():
    return {
        "footer_year": YEAR,
        "footer_author": "andy489",
    }


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=post_objects, )


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, )


if __name__ == "__main__":
    app.run(debug=True)
