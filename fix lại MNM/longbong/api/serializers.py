from rest_framework import serializers
from .models import *

class NguoiDungSerializer(serializers.ModelSerializer):
    class Meta:
        model = NguoiDung
        fields = '__all__'

class SanPhamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanPham
        fields = '__all__'

class GioHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = GioHang
        fields = '__all__'

class ChiTietGioHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietGioHang
        fields = '__all__'

class DonHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonHang
        fields = '__all__'

class ChiTietDonHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietDonHang
        fields = '__all__'

class ThanhToanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThanhToan
        fields = '__all__'

class DanhGiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanhGia
        fields = '__all__'

