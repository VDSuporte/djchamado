# contas/urls.py

from django.urls import path
from . import views
from .views import request_password_reset_view, verify_reset_code_view, reset_password_view
from .views import change_username_view
from .views import delete_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='usuarios'),
    path('registrar/', views.register_view, name='registrar'),
    path('verify_email/', views.verify_email_view, name='verify_email'),
    path('users/', views.user_list_view, name='user-list'),  # Adicione esta linha
    path('request-password-reset/', request_password_reset_view, name='request_password_reset'),
    path('verify-reset-code/', verify_reset_code_view, name='verify_reset_code'),
    path('reset-password/', reset_password_view, name='reset_password'),
    path('change-username/', change_username_view, name='change_username'),
    path('delete-user/', delete_user, name='delete_user'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='usuarios'),
]
