from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        # TODO not working save to db

    def save_as_staff(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True

        if commit:
            user.save()
        return user