import os
from datetime import timedelta

class Config:
    # Cấu hình bảo mật
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-very-secret'
    
    # Cấu hình SQLAlchemy
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Cấu hình Upload
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/img')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} 