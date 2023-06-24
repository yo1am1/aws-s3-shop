from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, "user": request.user})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(
                request, username=username, password=password
            )
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "login.html", {"user": request.user})
    return render(request, "login.html", {"user": request.user})


def index(request):
    return render(request, "index.html", {"user": request.user})


def logout(request):
    logout(request)
    return render(redirect("home"))
