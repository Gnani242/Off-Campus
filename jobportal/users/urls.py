from django.urls import path

from .views import (
    UserLoginView,
    UserLogoutView,
    register,
    dashboard,
    profile,
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
]

