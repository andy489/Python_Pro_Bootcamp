from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
# Import models AFTER db creation but before first use
from models import User, BlogPost, Comment

login_manager = LoginManager()
bootstrap = Bootstrap5()
ckeditor = CKEditor()


# Move the user_loader to a separate function
def init_login_manager(app):
    @login_manager.user_loader
    def load_user(user_id):
        from models.user import User  # Import here to avoid circular imports
        return db.session.get(User, int(user_id))

    login_manager.init_app(app)