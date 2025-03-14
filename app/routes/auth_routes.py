from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.actor import Actor
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('user_type')
        
        print(f"Login attempt - Email: {email}, Type: {user_type}")  # Debug log
        
        if user_type == 'actor':
            user = Actor.query.filter_by(email=email).first()
            print(f"Actor query result: {user}")  # Debug log
        else:
            user = User.query.filter_by(email=email).first()
            print(f"User query result: {user}")  # Debug log
            
        if user and user.check_password(password):
            login_user(user, remember=True)
            print(f"Login successful - Username: {user.username}, Type: {user.__class__.__name__}, ID: {user.id}")  # Debug log
            flash(f'Đăng nhập thành công! Xin chào {user.name or user.username}')
            return redirect(url_for('blog.home'))
            
        print("Login failed - Invalid credentials")  # Debug log
        flash('Email hoặc mật khẩu không đúng')
    return render_template('auth/login.html')

@auth_bp.route('/register/actor', methods=['GET', 'POST'])
def register_actor():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if Actor.query.filter_by(email=email).first():
            flash('Email đã tồn tại')
            return redirect(url_for('auth.register_actor'))
            
        if Actor.query.filter_by(username=username).first() or User.query.filter_by(username=username).first():
            flash('Tên đăng nhập đã tồn tại')
            return redirect(url_for('auth.register_actor'))
            
        actor = Actor(username=username, email=email)
        actor.set_password(password)
        db.session.add(actor)
        db.session.commit()
        
        flash('Đăng ký thành công! Vui lòng đăng nhập để tiếp tục.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register_actor.html')

@auth_bp.route('/register/user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash('Email đã tồn tại')
            return redirect(url_for('auth.register_user'))
            
        if User.query.filter_by(username=username).first() or Actor.query.filter_by(username=username).first():
            flash('Tên đăng nhập đã tồn tại')
            return redirect(url_for('auth.register_user'))
            
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Đăng ký thành công! Vui lòng đăng nhập để tiếp tục.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register_user.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.home'))