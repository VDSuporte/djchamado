from django.contrib import admin
from django.urls import path
from .views import ListagemView

urlpatterns = [
    path('listagens/', ListagemView.as_view(), name='listagens'),
]