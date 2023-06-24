from django.urls import path

from . import views
from .views import index, signup, login, logout_user


urlpatterns = [
    path("", index, name="home"),
    path("register/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout_user/", logout_user, name="logout"),
]
