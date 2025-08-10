import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    CKEDITOR_SERVE_LOCAL = True