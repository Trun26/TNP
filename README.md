Tải file về tiến hành giải nén
Mở folder sau khi giải nén trên Visual studio code
Vào file settings.py ở phần DATABASES tiến hành sửa đổi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quanlybanhang',
        'USER': 'postgres',
        'PASSWORD': 'Mật khẩu postgresql ',
        'HOST': ' # IP máy chủ postgresql',
        'PORT': '5432',
    }
}
