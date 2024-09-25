from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms.widgets import PasswordInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'input100',
                'placeholder': 'Логин',
                'type': "text",
                "name": "username"
            }
        ),
    )
    password = forms.CharField(
        label='Пароль1',
        strip=False,
        widget=PasswordInput(
            attrs={
                'class': 'input100',
                'placeholder': 'Пароль',
                'type': 'password',
                "name": "pass"
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

