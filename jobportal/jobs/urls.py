from django.urls import path

from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("recommended/", views.recommended_jobs, name="recommended_jobs"),
]

