from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import caulong
from .serializers import caulongSerializer
from .models import Nguoidung
from .serializers import NguoidungSerializer

class caulongListCreate(generics.ListCreateAPIView):
    queryset = caulong.objects.all()
    serializer_class = caulongSerializer

    def delete(self, request, *args, **kwargs):
        caulong.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class caulongRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = caulong.objects.all()
    serializer_class = caulongSerializer
    lookup_field = "pk"


class NguoidungListCreate(generics.ListCreateAPIView):
    queryset = Nguoidung.objects.all()
    serializer_class = NguoidungSerializer

    def delete(self, request, *args, **kwargs):
        Nguoidung.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NguoidungRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nguoidung.objects.all()
    serializer_class = NguoidungSerializer
    lookup_field = "pk"