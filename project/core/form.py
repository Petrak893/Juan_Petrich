from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"}),
                   "password": forms.PasswordInput(attrs={"class": "form-control"}),
                   }


class CustomUserCreationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_texts = {k: "" for k in fields}
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"}),
                   "password1": forms.PasswordInput(attrs={"class": "form-control"}),
                   "password2": forms.PasswordInput(attrs={"class": "form-control"}),
                   }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile_picture = self.cleaned_data.get('profile_picture')
            profile = Profile.objects.create(user=user, profile_picture=profile_picture)
        return user
