from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from jobs.models import Job
from .models import Application


@login_required
def apply_to_job(request, job_id: int):
    job = get_object_or_404(Job, id=job_id)
    application, created = Application.objects.get_or_create(
        user=request.user,
        job=job,
    )
    if created:
        messages.success(request, "Application saved successfully.")
    else:
        messages.info(request, "You have already applied for this job.")
    return redirect("applied_jobs")


@login_required
def applied_jobs(request):
    applications = (
        Application.objects.select_related("job")
        .filter(user=request.user)
        .order_by("-applied_date")
    )
    return render(request, "applications/applied_jobs.html", {"applications": applications})

