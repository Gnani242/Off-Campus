from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models


def user_resume_upload_to(instance: "User", filename: str) -> str:
    return f"resumes/user_{instance.id}/{filename}"


class User(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True)
    skills = models.TextField(
        blank=True,
        help_text="Comma-separated list of skills, e.g. Python, Django, SQL",
    )
    resume = models.FileField(upload_to=user_resume_upload_to, blank=True, null=True)
    preferred_location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def skill_list(self) -> list[str]:
        if not self.skills:
            return []
        return [s.strip().lower() for s in self.skills.split(",") if s.strip()]

    def __str__(self) -> str:
        return self.username

