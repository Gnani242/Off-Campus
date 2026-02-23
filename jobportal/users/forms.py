from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=150, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "full_name", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("full_name", "email", "skills", "preferred_location", "resume")
        widgets = {
            "skills": forms.Textarea(
                attrs={"rows": 3, "placeholder": "e.g. Python, Django, SQL"}
            )
        }

