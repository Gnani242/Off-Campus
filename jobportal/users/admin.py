from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "full_name", "preferred_location", "created_at")
    search_fields = ("username", "email", "full_name", "skills")

