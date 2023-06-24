from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from login.forms import SignUpForm
from django.core.mail import send_mail

from login.tokens import account_activation_token


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # don't save to db yet
            user.is_active = False
            user.save()  # save to db
            current_site = get_current_site(request)
            message = render_to_string(
                "account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                },
            )
            user.email_user("Validation", message)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form, "user": request.user})


def index(request):
    if request.method == "POST" and "Logout" in request.POST:
        logout(request)
        return redirect("home")
    return render(request, "index.html", {"user": request.user})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("home")
    else:
        return render(request, "account_activation_invalid.html")
