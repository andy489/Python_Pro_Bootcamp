from extensions import db

# Import all models here to ensure they're registered with SQLAlchemy
from .user import User
from .blog_post import BlogPost
from .comment import Comment

__all__ = ['User', 'BlogPost', 'Comment', 'db']