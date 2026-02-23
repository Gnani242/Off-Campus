from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from jobs.services import get_recommended_jobs_for_user
from .forms import UserRegisterForm, UserProfileForm
from .models import User


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    next_page = "login"


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user: User = form.save()
            messages.success(request, "Account created successfully. You can log in now.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def dashboard(request):
    recommended_jobs = get_recommended_jobs_for_user(request.user)
    return render(
        request,
        "users/dashboard.html",
        {
            "recommended_jobs": recommended_jobs[:5],
        },
    )


@login_required
def profile(request):
    user: User = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = UserProfileForm(instance=user)
    return render(request, "users/profile.html", {"form": form})

