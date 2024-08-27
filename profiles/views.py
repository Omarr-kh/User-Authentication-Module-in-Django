from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="login")
def home_page(request):
    return render(request, "home.html")


def register_page(request):
    form = RegisterForm()
    context = {"form": form}

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Account Created for {user}")
            return redirect("login")

    return render(request, "register.html", context)


def login_page(request):
    form = LoginForm()
    context = {"form": form}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or Password is incorrect")
    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect("login")
