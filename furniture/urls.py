from django.urls import path
from furniture import views

urlpatterns = [
    path("", views.MainView.as_view())
]