from flask_login import current_user

from models.comment import Comment
from models.blog_post import BlogPost
from extensions import db
from utils.decorators import admin_only

class BlogService:
    @staticmethod
    def get_all_posts():
        return db.session.execute(db.select(BlogPost).order_by(BlogPost.date.desc())).scalars().all()

    @staticmethod
    def get_post_by_id(post_id):
        return db.get_or_404(BlogPost, post_id)

    @staticmethod
    def create_post(form):
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=BlogPost.create_date_string()
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def update_post(post_id, form):
        post = db.get_or_404(BlogPost, post_id)
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.img_url = form.img_url.data
        post.author = current_user
        post.body = form.body.data
        db.session.commit()
        return post

    @staticmethod
    @admin_only
    def delete_post(post_id):
        post = BlogPost.query.get(post_id)
        if post:
            # Manually delete comments if cascade fails
            Comment.query.filter_by(post_id=post.id).delete()

            db.session.delete(post)
            db.session.commit()

    @staticmethod
    @admin_only
    def delete_comment(comment_id):
        comment = db.get_or_404(Comment, comment_id)
        db.session.delete(comment)
        db.session.commit()

        return comment.post_id