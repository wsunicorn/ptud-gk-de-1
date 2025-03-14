from flask import Blueprint, render_template, request
from app.models.post import Post
from app.models.comment import Comment

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=6)
    return render_template('blog/home.html', posts=posts)

@blog_bp.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    return render_template('blog/post_detail.html', post=post, comments=comments) 