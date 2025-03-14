from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Vui lòng đăng nhập để truy cập trang này.'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Khởi tạo các extension
    db.init_app(app)
    login_manager.init_app(app)

    # User loader cho cả Actor và User
    @login_manager.user_loader
    def load_user(user_id):
        # Thử tải Actor trước
        from app.models.actor import Actor
        actor = Actor.query.get(int(user_id))
        if actor:
            return actor
            
        # Nếu không phải Actor, thử tải User
        from app.models.user import User
        return User.query.get(int(user_id))

    # Đăng ký các blueprint
    from app.routes.auth_routes import auth_bp
    from app.routes.actor_routes import actor_bp
    from app.routes.user_routes import user_bp
    from app.routes.blog_routes import blog_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(actor_bp, url_prefix='/actor')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(blog_bp, url_prefix='/')

    return app 