from django.db import models

class NguoiDung(models.Model):
    LOAI_NGUOI_DUNG = [
        ('KhachHang', 'Khách Hàng'),
        ('QuanTriVien', 'Quản Trị Viên'),
    ]

    mand = models.AutoField(primary_key=True)  # SERIAL trong PostgreSQL
    hoten = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matkhau = models.CharField(max_length=255)
    sdt = models.CharField(max_length=15, blank=True, null=True)
    loainguoidung = models.CharField(max_length=20, choices=LOAI_NGUOI_DUNG, default='KhachHang')
    ngaytao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "nguoidung"  # Trùng với bảng trong PostgreSQL

class SanPham(models.Model):
    masp = models.AutoField(primary_key=True)
    tensp = models.CharField(max_length=255)
    mota = models.TextField(blank=True, null=True)
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    soluongtonkho = models.IntegerField(default=0)
    hinhanh = models.CharField(max_length=255, blank=True, null=True)
    danhmuc = models.CharField(max_length=100, blank=True, null=True)
    ngaytao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sanpham"

class GioHang(models.Model):
    magh = models.AutoField(primary_key=True)
    nguoidung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)

    class Meta:
        db_table = "giohang"

class ChiTietGioHang(models.Model):
    giohang = models.ForeignKey(GioHang, on_delete=models.CASCADE)
    sanpham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    soluong = models.IntegerField()

    class Meta:
        db_table = "chitietgiohang"
        unique_together = ('giohang', 'sanpham')

class DonHang(models.Model):
    TRANG_THAI_CHOICES = [
        ('ChoXacNhan', 'Chờ Xác Nhận'),
        ('DangGiao', 'Đang Giao'),
        ('HoanThanh', 'Hoàn Thành'),
        ('DaHuy', 'Đã Hủy'),
    ]

    madh = models.AutoField(primary_key=True)
    nguoidung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    ngaydathang = models.DateTimeField(auto_now_add=True)
    tongtien = models.DecimalField(max_digits=10, decimal_places=2)
    trangthai = models.CharField(max_length=20, choices=TRANG_THAI_CHOICES, default='ChoXacNhan')

    class Meta:
        db_table = "donhang"

class ChiTietDonHang(models.Model):
    donhang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    sanpham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    soluong = models.IntegerField()
    gia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "chitietdonhang"
        unique_together = ('donhang', 'sanpham')

class ThanhToan(models.Model):
    PHUONG_THUC_THANH_TOAN = [
        ('TienMat', 'Tiền Mặt'),
        ('ChuyenKhoan', 'Chuyển Khoản'),
        ('TheTinDung', 'Thẻ Tín Dụng'),
    ]

    TRANG_THAI_THANH_TOAN = [
        ('ChuaThanhToan', 'Chưa Thanh Toán'),
        ('DaThanhToan', 'Đã Thanh Toán'),
    ]

    matt = models.AutoField(primary_key=True)
    donhang = models.OneToOneField(DonHang, on_delete=models.CASCADE, unique=True)
    sotien = models.DecimalField(max_digits=10, decimal_places=2)
    phuongthucthanhtoan = models.CharField(max_length=20, choices=PHUONG_THUC_THANH_TOAN)
    trangthaithanhtoan = models.CharField(max_length=20, choices=TRANG_THAI_THANH_TOAN, default='ChuaThanhToan')
    ngaythanhtoan = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "thanhtoan"

class DanhGia(models.Model):
    madg = models.AutoField(primary_key=True)
    nguoidung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    sanpham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    sosao = models.IntegerField()
    binhluan = models.TextField(blank=True, null=True)
    ngaydanhgia = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "danhgia"
