"""Users urls"""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("singup/", views.SingUpView.as_view(), name="singup"),
    path("me/profile/", views.UpdateProfileView.as_view(), name="update_profile"),
    path("<str:username>/",views.UserDetailView.as_view(),name="detail"),
]
