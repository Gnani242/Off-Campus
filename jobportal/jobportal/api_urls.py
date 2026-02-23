from django.urls import path

from jobs.api_views import JobListAPI, RecommendedJobsAPI
from applications.api_views import ApplicationListCreateAPI
from users.api_views import ProfileAPI

urlpatterns = [
    path("jobs/", JobListAPI.as_view(), name="api_jobs"),
    path("recommended-jobs/", RecommendedJobsAPI.as_view(), name="api_recommended_jobs"),
    path("applications/", ApplicationListCreateAPI.as_view(), name="api_applications"),
    path("profile/", ProfileAPI.as_view(), name="api_profile"),
]

