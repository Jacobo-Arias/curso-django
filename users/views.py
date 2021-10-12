"""User views"""

from django.shortcuts import render, redirect

# Django

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Forms
from users.forms import ProfileForm, SingupForm

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
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feed")

    else:
        form = SingupForm()

    return render(
        request=request, template_name="users/singup.html", context={"form": form}
    )


@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect("login")


@login_required
def update_profile(request):
    """Update a user"""

    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            profile.website = data["website"]
            profile.phone_number = data["phone_number"]
            profile.biography = data["biography"]
            profile.picture = data["picture"]
            profile.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("feed")
        else:
            print("Error")
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name="users/update_profile.html",
        context={"profile": profile, "user": request.user, "form": form},
    )
