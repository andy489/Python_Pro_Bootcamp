import os
import smtplib

from flask import Blueprint, render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from forms.forms import ContactForm

main_bp = Blueprint('main', __name__)


@main_bp.route("/about")
def about():
    return render_template(template_name_or_list="about.html", current_user=current_user)


def create_contact_form():
    form = ContactForm()

    if current_user.is_authenticated:
        form.submit.render_kw = {
            'class': 'btn text-uppercase btn-success',
            'disabled': False
        }
    else:
        form.submit.render_kw = {
            'class': 'btn text-uppercase btn-danger',
            'disabled': True
        }
    return form


@main_bp.route(rule="/contact", methods=["GET", "POST"])
def contact():
    contact_form = create_contact_form()

    if contact_form.validate_on_submit():
        send_email(request)
        return redirect(url_for(endpoint='blog.get_all_posts'))

    return render_template(template_name_or_list="contact.html", msg_sent=False, form=contact_form)


MY_EMAIL = os.getenv("MY_EMAIL")
MY_MAIL_PASS = os.getenv("MY_EMAIL_PASS")


@login_required
def send_email(curr_request):
    data = curr_request.form

    name_ = data["name"]
    email_ = current_user.email
    phone_ = data["phone"]
    message_ = data["message"]

    email_message = f"Subject:New Message\n\nName: {name_}\nEmail: {email_}\nPhone: {phone_}\nMessage:{message_}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_MAIL_PASS)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)
