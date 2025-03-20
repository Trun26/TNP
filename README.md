## Cấu hình kết nối PostgreSQL trong Django
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

