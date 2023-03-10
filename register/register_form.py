from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        username = forms.CharField()
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        widgets = {'password': forms.PasswordInput()}
