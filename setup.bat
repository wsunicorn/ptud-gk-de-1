@echo off
echo ===== Setting up Blog Application =====

:: Kiểm tra Python đã được cài đặt chưa
python --version > nul 2>&1
if errorlevel 1 (
    echo Python is not installed! Please install Python from python.org
    pause
    exit
)

:: Hiển thị phiên bản Python
python --version
echo.

:: Kiểm tra và xóa môi trường ảo cũ nếu tồn tại
if exist venv (
    echo Removing existing virtual environment...
    rmdir /s /q venv
)

:: Tạo môi trường ảo mới
echo Creating new virtual environment...
python -m venv venv

:: Kích hoạt môi trường ảo
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Cài đặt các dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Thiết lập biến môi trường
echo Setting environment variables...
set FLASK_APP=app
set FLASK_ENV=development

:: Hiển thị thông tin tài khoản mẫu
echo.
echo ===== Sample Accounts =====
echo Actor: 
echo   - Email: actor@gmail.com
echo   - Password: 123456
echo.
echo User:
echo   - Email: user@gmail.com
echo   - Password: 123456
echo.
echo ===== Starting Application =====
echo Application will be available at http://127.0.0.1:5000
echo.

:: Chạy ứng dụng
python -m flask run 