# Thông tin cá nhân:

- Họ và tên: Nguyễn Ngọc Lân
- MSSV: 22635801
- STT: 83

# Blog Application

Ứng dụng blog đơn giản được xây dựng bằng Flask, cho phép Actor đăng bài và User bình luận.

## Tính năng

### Dành cho Actor (Người viết bài)

- Đăng ký và đăng nhập tài khoản Actor
- Quản lý thông tin cá nhân
- Tạo, chỉnh sửa và xóa bài viết
- Xem thống kê bài viết và bình luận
- Dashboard quản lý với giao diện trực quan

### Dành cho User (Người đọc)

- Đăng ký và đăng nhập tài khoản User
- Quản lý thông tin cá nhân
- Đọc bài viết
- Bình luận trên bài viết
- Quản lý bình luận cá nhân

### Tính năng chung

- Giao diện người dùng hiện đại và responsive
- Hệ thống xác thực người dùng an toàn
- Text avatar tự động từ tên người dùng
- Thống kê hoạt động
- Tìm kiếm và phân trang bài viết

## Công nghệ sử dụng

### Backend

- Python 3.x
- Flask Framework
- SQLAlchemy (ORM)
- Flask-Login (Xác thực người dùng)
- Jinja2 (Template Engine)

### Frontend

- Bootstrap 5
- Bootstrap Icons
- Custom CSS với hiệu ứng modern
- Responsive Design
- JavaScript cho tương tác người dùng

## Cài đặt và Chạy

1. Cài đặt Git và thiết lập repository:

```bash
# Cài đặt Git từ https://git-scm.com/downloads

# Thiết lập thông tin Git (thay thế bằng thông tin của bạn)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Clone repository
git clone https://github.com/wsunicorn/ptud-gk-de-1.git
cd ptud-gk-de-1

# Khởi tạo Git repository và branch main
git init
git checkout -b main
```

2. Cài đặt Python 3.x nếu chưa có:

- Tải Python từ [python.org](https://www.python.org/downloads/)
- Đảm bảo Python và pip đã được thêm vào PATH

3. Tạo và kích hoạt môi trường ảo:

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

4. Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

5. Thiết lập biến môi trường:

```bash
# Windows
set FLASK_APP=app
set FLASK_ENV=development

# Linux/Mac
export FLASK_APP=app
export FLASK_ENV=development
```

6. Chạy ứng dụng:

```bash
flask run
```
## Có thể click vào file 'setup.bat' để cài đặt ngay.

## Có thể click vào file 'setup.bat' để cài đặt ngay.

Ứng dụng sẽ chạy tại địa chỉ: `http://127.0.0.1:5000`

### Tài khoản mẫu có sẵn:

Actor:

- Email: actor@gmail.com
- Password: 123456

User:

- Email: user@gmail.com
- Password: 123456

### Làm việc với Git:

```bash
# Kiểm tra trạng thái
git status

# Thêm tất cả file mới và đã thay đổi
git add .

# Commit các thay đổi
git commit -m "Mô tả commit của bạn"

# Push lên repository
git push origin main

# Nếu gặp lỗi khi push, có thể cần force push (cẩn thận khi sử dụng)
git push -f origin main
```

## Cấu trúc thư mục

```
ptud-gk-de-1/                # Thư mục gốc
├── app/                     # Thư mục chính của ứng dụng
│   ├── __init__.py         # Khởi tạo ứng dụng Flask
│   ├── models/             # Models cho database
│   │   ├── __init__.py
│   │   ├── actor.py        # Actor model
│   │   ├── post.py         # Post model
│   │   ├── user.py         # User model
│   │   └── comment.py      # Comment model
│   ├── routes/             # Routes và views
│   │   ├── __init__.py
│   │   ├── actor_routes.py # Routes cho Actor
│   │   ├── auth_routes.py  # Routes xác thực
│   │   ├── blog_routes.py  # Routes cho blog
│   │   └── user_routes.py  # Routes cho User
│   ├── static/             # Static files
│   │   ├── css/           # CSS files
│   │   │   ├── main.css   # Styles chính
│   │   │   └── sidebar.css # Styles cho sidebar
│   │   └── js/            # JavaScript files
│   └── templates/          # Jinja2 templates
│       ├── actor/          # Templates cho Actor
│       │   ├── dashboard.html
│       │   ├── create_post.html
│       │   └── edit_post.html
│       ├── auth/           # Templates xác thực
│       │   ├── login.html
│       │   ├── register_actor.html
│       │   └── register_user.html
│       ├── blog/           # Templates cho blog
│       │   ├── home.html
│       │   └── post_detail.html
│       ├── user/           # Templates cho User
│       │   └── profile.html
│       └── base.html       # Template cơ sở
├── migrations/             # Database migrations
├── instance/              # Instance folder
│   └── blog.db           # SQLite database (có sẵn dữ liệu mẫu)
├── requirements.txt       # Dependencies
└── README.md             # Tài liệu dự án
```

## Tác giả

Nguyễn Ngọc Lân
