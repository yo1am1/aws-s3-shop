from django.urls import path

from . import views
from .views import index, signup


urlpatterns = [
    path("", index, name="home"),
    path("register/", signup, name="signup"),
]
