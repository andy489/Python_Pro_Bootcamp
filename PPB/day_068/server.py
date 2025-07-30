from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'API-SECRET-8AuT-ysoU-ySod-93vB'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route(rule='/')
def home():
    # Passing True or False if the user is authenticated.
    return render_template(template_name_or_list="index.html", logged_in=current_user.is_authenticated)


@app.route(rule='/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # Hashing and salting the password entered by the user
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )

        # Storing the hashed password in our database
        new_user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name'),
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for(endpoint="secrets", name=request.form.get('name')), )

    return render_template(template_name_or_list="register.html", logged_in=current_user.is_authenticated)


@app.route(rule='/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email entered
        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()

        if user is None:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))

        # Check stored password hash against entered password hashed
        if not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('secrets', name=request.form.get('name')))

    return render_template(template_name_or_list="login.html", logged_in=current_user.is_authenticated)


@app.route(rule='/secrets')
@login_required
def secrets():
    print(current_user.name)
    # Passing the name from the current_user
    return render_template(template_name_or_list="secrets.html", name=current_user.name, logged_in=True)


@app.route(rule='/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Only logged-in users can download the pdf
@app.route(rule='/download')
@login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf',
                               # as_attachment=True
                               )


if __name__ == "__main__":
    app.run(debug=True)
