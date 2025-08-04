import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '8BYkEfBA6O6donzWlSihBXox7C0sKR6b')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///posts.db')
    CKEDITOR_SERVE_LOCAL = True