"""User views"""

from django.shortcuts import render, redirect, get_object_or_404

# Django

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views

# Views
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Posts
from users.models import Profile

# Forms
from users.forms import SingupForm

# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = "users/detail.html"
    slug_field = "username"
    # el campo slug_url_kwarg es el que tiene el path en el url
    # luego del str en el <str:[]>
    # para este caso es <str:username> y por eso slug_url_kwarg es username
    slug_url_kwarg = "username"
    context_object_name = "user"
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Posts.objects.filter(user=user).order_by("-created")
        return context


class LoginView(auth_views.LoginView):
    """Login class view"""

    template_name = "users/login.html"
    redirect_authenticated_user = True


class SingUpView(FormView):
    """User sing up view."""

    template_name = "users/singup.html"
    form_class = SingupForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """Save singup form data"""
        form.save()
        username = form["username"].value()
        password = form["password"].value()

        user = authenticate(self.request, username=username, password=password)

        login(self.request, user)
        return super().form_valid(form)


class LogoutView(auth_views.LogoutView, LoginRequiredMixin):
    """Logout class view"""

    pass


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update a user"""

    template_name = "users/update_profile.html"
    model = Profile
    fields = ["website", "biography", "phone", "picture"]

    def get_object(self):
        """Return user's  profile"""
        return self.request.user.profile

    def get_success_url(self):
        """return ro user's profile"""
        username = self.object.user.username
        return reverse("users:detail", kwargs={"username": username})


def Follow(request, username):
    """Vista para dar like a un post"""
    profile = get_object_or_404(User, username=username)
    profile = profile.profile
    user = request.user.profile
    user.follow.add(profile)
    return redirect(reverse("users:detail", kwargs={"username": profile.user.username}))

def Unfollow(request, username):
    """Vista para quitar el like a un post"""
    profile = get_object_or_404(User, username=username)
    profile = profile.profile
    user = request.user.profile
    user.follow.remove(profile)
    return redirect(reverse("users:detail", kwargs={"username": profile.user.username}))

