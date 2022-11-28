from django import forms
from .models import Document
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

        
class CloudUser(UserCreationForm):
  
    # acces = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(CloudUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user