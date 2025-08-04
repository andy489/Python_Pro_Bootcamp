from flask import flash, redirect, url_for
from flask_login import current_user
from models.comment import Comment
from extensions import db

class CommentService:
    @staticmethod
    def add_comment(form, post_id):
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return False

        new_comment = Comment(
            text=form.comment_text.data,
            comment_author=current_user,
            post_id=post_id
        )

        db.session.add(new_comment)
        db.session.commit()
        return True