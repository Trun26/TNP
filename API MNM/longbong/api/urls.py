from django.urls import path
from . import views
from api.models import Nguoidung
from rest_framework.response import Response

urlpatterns = [
    path("caulongs/", views.caulongListCreate.as_view(), name="caulong-view-create"),
    path(
        "caulongs/<int:pk>/",
        views.caulongRetrieveUpdateDestory.as_view(),
        name="update",
    ),
]
urlpatterns = [
    path("nguoidungs/", views.NguoidungListCreate.as_view(), name="nguoidung-view-create"),
    path("nguoidungs/<int:pk>/", views.NguoidungRetrieveUpdateDestroy.as_view(), name="update"),
]
