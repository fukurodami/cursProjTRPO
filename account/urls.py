
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # post views
    path("login/", views.user_login, name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]