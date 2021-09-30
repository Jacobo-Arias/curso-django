from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# models
from django.contrib.auth.models import User
from users.models import Profile

#utils
from django.db.utils import IntegrityError

# Create your views here.


def login_view(request):
    """Login view"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("feed")
        else:
            return render(
                request, "users/login.html", {"error": "Invalid email or password "}
            )

    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect("feed")
    return render(request, "users/login.html")


def singup_view(request):
    """Sing up view"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["password_confirmation"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        if password != confirm_password:
            return render(request, "users/singup.html", {"error":"Password confirmation does not match"})

        else:
            try:
                user = User.objects.create_user(username=username,password=password)
            except IntegrityError:
                return render(request, "users/singup.html", {"error":"Username already taken"})
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            profile = Profile(user=user)
            profile.save()

            login(request,user)
            redirect("login")

    elif request.method == "GET":
        if request.user.is_authenticated:
            return redirect("feed")

    return render(request, "users/singup.html")


@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect("login")

@login_required
def update_profile(request):
    """Update a user"""

    return render(request,"users/update_profile.html")