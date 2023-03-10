from django import forms
from .models import SignIn


class LoginForm(forms.ModelForm):
    class Meta:
        model = SignIn
        # fields = '__all__'  # Inherating all the fields from class Signin() model.py
        username = forms.CharField()
        password = forms.PasswordInput()
        fields = ['username', 'password']

        # Password field chars won't display
        widgets = {'password': forms.PasswordInput()}
