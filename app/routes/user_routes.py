from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.comment import Comment
from app.models.post import Post

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile')
@login_required
def profile():
    comments = Comment.query.filter_by(user_id=current_user.id).order_by(Comment.created_at.desc()).all()
    return render_template('user/profile.html', comments=comments)

@user_bp.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    # Kiểm tra xem người dùng có phải là User không
    if current_user.__class__.__name__ != 'User':
        flash('Chỉ User mới có thể bình luận!')
        return redirect(url_for('blog.post_detail', post_id=post_id))

    post = Post.query.get_or_404(post_id)
    content = request.form.get('content', '').strip()
    
    # Kiểm tra nội dung bình luận
    if not content:
        flash('Nội dung bình luận không được để trống!')
        return redirect(url_for('blog.post_detail', post_id=post_id))
    
    if len(content) > 1000:  # Giới hạn 1000 ký tự
        flash('Nội dung bình luận không được vượt quá 1000 ký tự!')
        return redirect(url_for('blog.post_detail', post_id=post_id))
    
    # Tạo và lưu bình luận
    comment = Comment(content=content, post_id=post_id, user_id=current_user.id)
    db.session.add(comment)
    db.session.commit()
    flash('Bình luận đã được thêm thành công!')
    return redirect(url_for('blog.post_detail', post_id=post_id))

@user_bp.route('/comment/<int:comment_id>/delete')
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.user_id != current_user.id:
        flash('Bạn không có quyền xóa bình luận này')
        return redirect(url_for('blog.post_detail', post_id=comment.post_id))
        
    post_id = comment.post_id
    db.session.delete(comment)
    db.session.commit()
    flash('Bình luận đã được xóa!')
    return redirect(url_for('blog.post_detail', post_id=post_id)) 