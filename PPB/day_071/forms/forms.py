from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()],
                       render_kw={
                           'class': 'form-control',
                           'placeholder': 'Enter your name...',
                           'id': 'name'
                       })

    phone = StringField('Phone Number', validators=[DataRequired()],
                        render_kw={
                            'class': 'form-control',
                            'placeholder': 'Enter your phone number...',
                            'id': 'phone',
                            'type': 'tel'
                        })

    message = TextAreaField('Message', validators=[DataRequired()],
                            render_kw={
                                'class': 'form-control',
                                'placeholder': 'Enter your message here...',
                                'id': 'message',
                                'style': 'height: 12rem'
                            })

    submit = SubmitField('SEND',
                         render_kw={
                             'class': 'btn text-uppercase',
                             'id': 'submitButton'
                         })
