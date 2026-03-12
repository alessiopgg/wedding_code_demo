from django.urls import path

from .views import home

app_name = "wedding"

urlpatterns = [
    path("", home, name="home"),
]
