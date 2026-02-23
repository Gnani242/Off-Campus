from __future__ import annotations

from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=150, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    required_skills = models.TextField(
        help_text="Comma-separated skills required for this job"
    )
    job_link = models.URLField()
    posted_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def required_skill_list(self) -> list[str]:
        return [
            s.strip().lower()
            for s in self.required_skills.split(",")
            if s.strip()
        ]

    def __str__(self) -> str:
        return f"{self.title} - {self.company_name}"

