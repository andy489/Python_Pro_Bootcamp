# from flask import Flask
#
# def create_app():
#     app = Flask(__name__)
#
#     # Load configuration
#     app.config.from_object("config.Config")
#
#     # Initialize extensions
#     from extensions import db, login_manager, bootstrap, ckeditor
#     db.init_app(app)
#     login_manager.init_app(app)
#     bootstrap.init_app(app)
#     ckeditor.init_app(app)
#
#     # Initialize gravatar
#     from utils.gravatar import init_gravatar
#     init_gravatar(app)
#
#     # Register blueprints
#     from routes.auth_routes import auth_bp
#     from routes.blog_routes import blog_bp
#     from routes.main_routes import main_bp
#
#     app.register_blueprint(auth_bp)
#     app.register_blueprint(blog_bp)
#     app.register_blueprint(main_bp)
#
#     return app