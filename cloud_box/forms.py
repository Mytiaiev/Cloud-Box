from django import forms
from .models import Document
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class CloudUser(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1")
