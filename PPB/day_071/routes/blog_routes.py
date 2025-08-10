from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms.forms import CreatePostForm, CommentForm
from services.blog_service import BlogService
from services.comment_service import CommentService
from utils import admin_only

blog_bp = Blueprint('blog', __name__)


@blog_bp.route(rule='/')
def get_all_posts():
    posts = BlogService.get_all_posts()
    return render_template(template_name_or_list="index.html", all_posts=posts, current_user=current_user)


@blog_bp.route(rule="/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    post = BlogService.get_post_by_id(post_id)
    form = CommentForm()

    if form.validate_on_submit():
        if not CommentService.add_comment(form, post_id):
            return redirect(url_for(endpoint='auth.login'))
    return render_template(template_name_or_list="post.html", post=post, current_user=current_user, form=form)


@blog_bp.route(rule="/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        BlogService.create_post(form)
        return redirect(url_for(endpoint="blog.get_all_posts"))
    return render_template(template_name_or_list="make-post.html", form=form, current_user=current_user)


@blog_bp.route(rule="/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogService.get_post_by_id(post_id)
    form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if form.validate_on_submit():
        BlogService.update_post(post_id, form)
        return redirect(url_for(endpoint="blog.show_post", post_id=post.id))
    return render_template(template_name_or_list="make-post.html", form=form, is_edit=True, current_user=current_user)


@blog_bp.route("/delete-post/<int:post_id>")
@login_required
def delete_post(post_id):
    BlogService.delete_post(post_id)
    return redirect(url_for(endpoint='blog.get_all_posts'))


@blog_bp.route("/delete-comment/<int:comment_id>")
@login_required
def delete_comment(comment_id):
    post_id = BlogService.delete_comment(comment_id)
    return redirect(url_for(endpoint='blog.show_post', post_id=post_id))
