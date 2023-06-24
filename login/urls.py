from django.urls import path

from . import views
from .views import index, signup, login


urlpatterns = [
    path("", index, name="home"),
    path("register/", signup, name="signup"),
    path("login/", login, name="login"),
]
