from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dangky/', views.dangky, name="dangky"),
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    path('dangxuat/', views.dangxuat, name='dangxuat'),
    path('copyright/', views.copyright_info_view, name='copyright-info'),
    path('read', views.read_book, name='read'),
    path('best_sellers/', views.best_sellers_view, name='best-sellers'),
]
