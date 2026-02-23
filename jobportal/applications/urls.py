from django.urls import path

from . import views

urlpatterns = [
    path("apply/<int:job_id>/", views.apply_to_job, name="apply_to_job"),
    path("my/", views.applied_jobs, name="applied_jobs"),
]

