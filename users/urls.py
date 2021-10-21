"""Users urls"""

# Django
from django.urls import path

# Views
from django.views.generic import TemplateView
from users import views

urlpatterns = [
    path("profile/<str:username>/",TemplateView.as_view(template_name="users/detail.html")),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("singup/", views.singup_view, name="singup"),
    path("me/profile/", views.update_profile, name="update_profile"),
]
