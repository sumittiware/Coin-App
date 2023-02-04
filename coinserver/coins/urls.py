from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<str:coin_id>', views.detail, name="detail")
]
