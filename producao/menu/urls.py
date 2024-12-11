from django.contrib import admin
from django.urls import path
from .views import IndexView
from . import views

urlpatterns = [
    path('menu/', IndexView.as_view(), name='menu'),
    path('error/', views.my_view, name='error'),
]