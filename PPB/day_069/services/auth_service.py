from flask import flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from extensions import db

class AuthService:
    @staticmethod
    def register_user(form):
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('auth.login'))

        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("blog.get_all_posts"))

    @staticmethod
    def login_user(form):
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return False
        if not check_password_hash(user.password, form.password.data):
            flash('Password incorrect, please try again.')
            return False
        login_user(user)
        return True