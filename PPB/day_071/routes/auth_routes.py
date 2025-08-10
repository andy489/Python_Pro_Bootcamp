from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import logout_user, current_user
from forms.forms import RegisterForm, LoginForm
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)


@auth_bp.route(rule='/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return AuthService.register_user(form)
    return render_template(template_name_or_list="register.html", form=form, current_user=current_user)


@auth_bp.route(rule='/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if AuthService.login_user(form):
            return redirect(url_for(endpoint='blog.get_all_posts'))
    return render_template(template_name_or_list="login.html", form=form, current_user=current_user)


@auth_bp.route(rule='/logout')
def logout():
    logout_user()
    return redirect(url_for(endpoint='blog.get_all_posts'))
