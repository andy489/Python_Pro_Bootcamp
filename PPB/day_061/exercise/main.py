from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message='Field must be at least 8 characters long')
    ])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "consistency"


@app.route("/")
def home():
    return render_template('index.html')


@app.route(rule="/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect('success')
    else:
        return redirect('denied')
        # return render_template(template_name_or_list="login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
