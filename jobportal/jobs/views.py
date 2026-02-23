from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Job
from .services import get_recommended_jobs_for_user


def home(request):
    jobs = Job.objects.order_by("-posted_date")[:10]
    return render(request, "jobs/home.html", {"jobs": jobs})


@login_required
def job_list(request):
    qs = Job.objects.order_by("-posted_date")
    search = request.GET.get("search")
    location = request.GET.get("location")

    if search:
        qs = qs.filter(title__icontains=search)
    if location:
        qs = qs.filter(location__icontains=location)

    paginator = Paginator(qs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "jobs/job_list.html",
        {"page_obj": page_obj, "search": search or "", "location": location or ""},
    )


@login_required
def recommended_jobs(request):
    recommendations = get_recommended_jobs_for_user(request.user)
    paginator = Paginator(recommendations, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "jobs/recommended_jobs.html",
        {"page_obj": page_obj},
    )

