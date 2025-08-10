import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_KEY', '8BYkEfBA6O6donzWlSihBXox7C0sKR6b')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI', 'sqlite:///posts.db')
    CKEDITOR_SERVE_LOCAL = True