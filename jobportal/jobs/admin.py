from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name", "location", "posted_date")
    search_fields = ("title", "company_name", "location", "required_skills")
    list_filter = ("location", "posted_date")

