from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
from dotenv import load_dotenv
import os
import data

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = os.getenv("MOVIE_DB_API_KEY")

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'consistency'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    __tablename__ = "my_movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        attrs = {key: value for key, value in self.__dict__.items() if not key.startswith('__') and not callable(value)}
        return f"{self.__class__.__name__}({attrs!r})"


with app.app_context():
    db.create_all()

with app.app_context():
    # Uncomment below to populate with all 10 movies
    # Movie.query.delete()

    if not Movie.query.first():
        for data in data.my_top_10:
            db.session.add(Movie(title=data[0], year=data[1], description=data[2], rating=data[3], ranking=data[4],
                                 review=data[5], img_url=data[6], ))
        db.session.commit()
        print("Added top 10 movies to the database")
    else:
        print("Database already contains data - skipping addition of movies")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    sz = len(all_movies)
    for i in range(sz):
        all_movies[i].ranking = sz - i
    db.session.commit()

    return render_template(template_name_or_list="index.html", movies=all_movies)


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired(), ])
    review = StringField("Your Review", validators=[DataRequired(), Length(min=1, max=250)])
    submit = SubmitField("Done")

    def set_dynamic_placeholders(self, curr_movie):
        """Set form field values based on movie data and set placeholders based on movie data"""

        self.rating.data = str(curr_movie.rating)
        self.review.data = curr_movie.review or ""

        self.rating.render_kw = {'placeholder': f'{curr_movie.rating}'}
        self.review.render_kw = {'placeholder': f'{curr_movie.review or "No review yet"}'}


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    curr_movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        try:
            curr_movie.rating = float(form.rating.data)
        except ValueError:
            # If conversion fails, keep the original rating
            pass
        curr_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    # Only set placeholders on GET request or when form isn't validated
    if request.method == "GET" or not form.is_submitted():
        form.set_dynamic_placeholders(curr_movie)

    return render_template(template_name_or_list="edit.html",
                           curr_movie=curr_movie,
                           form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    curr_movie = db.get_or_404(Movie, movie_id)
    db.session.delete(curr_movie)
    db.session.commit()
    return redirect(url_for("home"))


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template(template_name_or_list="add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={
            "api_key": MOVIE_DB_API_KEY, "language": "en-US",
        })
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
        )
        print(new_movie)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
