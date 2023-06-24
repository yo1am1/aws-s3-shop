from django.urls import path

from . import views
from .views import index, signup, activate

urlpatterns = [
    path("", index, name="home"),
    path("register/", signup, name="signup"),
    path(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        activate,
        name="activate",
    ),
]
