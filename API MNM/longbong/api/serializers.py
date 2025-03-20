from rest_framework import serializers
from .models import caulong
from .models import Nguoidung

class caulongSerializer(serializers.ModelSerializer):
    class Meta:
        model = caulong
        fields = ["id", "title", "content", "published_date"]

class NguoidungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nguoidung
        fields = ["MaND", "Hoten", "Email", "Matkhau", "SDT", "Loainguoidung", "NgayTao"]