# forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, required=True, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, max_length=30, required=True, label='Contraseña')
