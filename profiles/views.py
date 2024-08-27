from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="login")
def home_view(request):
    """
    View to render the home page.
    Only accessible to authenticated users.
    """
    return render(request, "home.html")


def register_view(request):
    """
    View to handle user registration.

    Process form data and register a user into the database
    Displays a success message if the account is created successfully
    """
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


def login_view(request):
    """
    View to handle user login.

    Processes form data and logs in a user if authenticated.
    If authentication fails, an error message is displayed.
    """
    form = LoginForm()
    context = {"form": form}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or Password is incorrect")

    return render(request, "login.html", context)


@login_required(login_url="login")
def logout_view(request):
    """
    View to handle user logout.

    Logs out the current user and redirects them to the login page.
    """
    logout(request)
    return redirect("login")
