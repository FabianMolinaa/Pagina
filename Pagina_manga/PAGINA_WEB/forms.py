# forms.py
from django import forms
from .models import  Usuario
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):
   pass