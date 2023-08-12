from django.urls import path
from . import views

urlpatterns = [
    # URL and view function defined in views.py
    path('', views.home),
]