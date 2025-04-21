from django import forms
from .models import Expense
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.models import User


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["title", "category", "amount", "date", "time"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "amount": forms.NumberInput(attrs={"step": "0.01", "class": "form-control"}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"}
        ),
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
