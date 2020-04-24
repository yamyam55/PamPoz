from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r"home", views.home_page, name="home_page")
]