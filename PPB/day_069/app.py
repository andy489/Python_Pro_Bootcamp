from flask import Flask
from datetime import datetime

from sqlalchemy import event

from init_db import seed_database
from models import User


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("config.Config")

    # Initialize extensions
    from extensions import db, bootstrap, ckeditor, init_login_manager

    db.init_app(app)
    with app.app_context():
        db.create_all()

        # Modern way to check tables
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        print("Tables created:", inspector.get_table_names())

        has_users = db.session.query(User.query.exists()).scalar()
        if not has_users:
            seed_database()

        # Enable SQLite foreign keys
        @event.listens_for(db.engine, "connect")
        def set_sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

    bootstrap.init_app(app)
    ckeditor.init_app(app)
    init_login_manager(app)

    # Initialize gravatar
    from utils.gravatar import init_gravatar
    init_gravatar(app)

    # Register blueprints
    from routes.auth_routes import auth_bp
    from routes.blog_routes import blog_bp
    from routes.main_routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(main_bp)

    return app


app = create_app()

curr_year = datetime.now().year

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    if value is None:
        return ""
    return value.strftime(format)

@app.context_processor
def inject_footer_data():
    return {
        "curr_year": curr_year,
    }


# Register the context processor
app.context_processor(inject_footer_data)

if __name__ == "__main__":
    # app.run(debug=False, port=5000)
    app.run(debug=True, host="0.0.0.0", port=5001)
    # ipconfig getifaddr en0
