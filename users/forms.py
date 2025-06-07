from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = (
            'username',
            "email",
            "password1",
            "password2",
        )


class VerificationForm(forms.Form):
    code = forms.CharField(
        label='Код подтверждения',
        max_length=6
    )
