from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
import requests
from app import db
from app.models.post import Post

actor_bp = Blueprint('actor', __name__)

def get_random_image():
    """Lấy URL hình ảnh ngẫu nhiên từ picsum.photos"""
    width, height = 800, 400
    return f"https://picsum.photos/{width}/{height}"

@actor_bp.route('/dashboard')
@login_required
def dashboard():
    posts = Post.query.filter_by(actor_id=current_user.id).order_by(Post.created_at.desc()).all()
    return render_template('actor/dashboard.html', posts=posts)

@actor_bp.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        # Lấy URL hình ảnh ngẫu nhiên
        image_url = get_random_image()
        
        post = Post(title=title, content=content, image_url=image_url, actor_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        
        flash('Bài viết đã được tạo thành công!')
        return redirect(url_for('actor.dashboard'))
    return render_template('actor/create_post.html')

@actor_bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.actor_id != current_user.id:
        flash('Bạn không có quyền chỉnh sửa bài viết này')
        return redirect(url_for('blog.home'))
        
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        db.session.commit()
        flash('Bài viết đã được cập nhật!')
        return redirect(url_for('actor.dashboard'))
    return render_template('actor/edit_post.html', post=post)

@actor_bp.route('/post/<int:post_id>/delete')
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.actor_id != current_user.id:
        flash('Bạn không có quyền xóa bài viết này')
        return redirect(url_for('blog.home'))
        
    db.session.delete(post)
    db.session.commit()
    flash('Bài viết đã được xóa!')
    return redirect(url_for('actor.dashboard')) 