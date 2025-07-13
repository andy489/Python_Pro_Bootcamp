from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.exc import StatementError

app = Flask(__name__)


## CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books_db.db"
app.secret_key = 'curiosity'

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialize the app with the extension
db.init_app(app)


## CREATE TABLE
class Book(db.Model):
    __tablename__ = "my_books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route(rule="/")
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template(template_name_or_list="index.html", books=all_books)


@app.route(rule="/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for(endpoint="home"))
        except StatementError:
            flash('Error: Invalid input', 'error')
            return redirect(url_for(endpoint='home'))
    return render_template(template_name_or_list="add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for(endpoint='home'))

    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template(template_name_or_list="edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for(endpoint='home'))


if __name__ == "__main__":
    app.run(debug=True)
