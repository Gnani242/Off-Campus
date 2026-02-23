from __future__ import annotations

from datetime import date
from typing import Iterable

from django.db.models import QuerySet

from users.models import User
from .models import Job


def calculate_match_percentage(user: User, job: Job) -> float:
    user_skills = set(user.skill_list())
    job_skills = set(job.required_skill_list())
    if not job_skills:
        return 0.0
    intersection = user_skills.intersection(job_skills)
    return round((len(intersection) / len(job_skills)) * 100, 2)


def get_recommended_jobs_for_user(user: User, min_match: float = 50.0) -> list[tuple[Job, float]]:
    if not user.is_authenticated:
        return []

    qs: QuerySet[Job] = Job.objects.all().order_by("-posted_date")
    results: list[tuple[Job, float]] = []
    for job in qs:
        match_pct = calculate_match_percentage(user, job)
        if match_pct >= min_match:
            results.append((job, match_pct))
    return results


def fetch_and_store_jobs_from_api(raw_jobs: Iterable[dict]) -> int:
    """
    Placeholder for integrating with a real job API.
    Accepts iterable of dicts and upserts jobs while avoiding duplicates.
    """
    created_count = 0
    for item in raw_jobs:
        job, created = Job.objects.get_or_create(
            title=item.get("title", ""),
            company_name=item.get("company_name", ""),
            job_link=item.get("job_link", ""),
            defaults={
                "location": item.get("location", ""),
                "salary": item.get("salary", ""),
                "required_skills": item.get("required_skills", ""),
                "posted_date": item.get("posted_date", date.today()),
            },
        )
        if created:
            created_count += 1
    return created_count

