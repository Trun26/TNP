from django.db import models

# Create your models here.
class caulong(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Nguoidung(models.Model):
    LOAI_NGUOI_DUNG = [
        ('KhachHang', 'Khách Hàng'),
        ('QuanTriVien', 'Quản Trị Viên')
    ]

    MaND = models.AutoField(primary_key=True)
    Hoten = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Matkhau = models.CharField(max_length=255)
    SDT = models.CharField(max_length=15, blank=True, null=True)
    Loainguoidung = models.CharField(
        max_length=20,
        choices=LOAI_NGUOI_DUNG,
        default='KhachHang'
    )
    NgayTao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Hoten

    