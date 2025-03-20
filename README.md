## Tải và cài đặt PostgreSQ
1.Tải và cài đặt PostgreSQL từ trang chính thức: PostgreSQL Download
2.Cấu hình PostgreSQL, ghi nhớ thông tin username và password.
## Import database từ file SQL Dùng pgAdmin
1.Mở pgAdmin và kết nối với PostgreSQL.
2.Tạo database mới với tên quanlybanhang.
3.Chọn database quanlybanhang, vào Tools → Query Tool.
4.Mở file quanlybanhang.sql và nhấn Execute để chạy.
## Nếu chưa cài đặt Cài đặt PostgreSQL driver cho Django
chạy lệnh trên new terminal của visual studio code
pip install psycopg2-binary

## cấu hình kết nối PostgreSQL trong Django
Sau khi tải file về, thực hiện các bước sau:
1. Giải nén file đã tải về.
2. Mở thư mục đã giải nén trong Visual Studio Code.
3. Mở file `settings.py` và cập nhật phần cấu hình DATABASES như sau:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quanlybanhang',
        'USER': 'postgres',
        'PASSWORD': 'Mật khẩu postgresql',
        'HOST': 'IP máy chủ postgresql',
        'PORT': '5432',
    }
}

