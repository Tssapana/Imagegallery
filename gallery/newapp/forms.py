from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image_file']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100, label="username")
    password=forms.CharField(max_length=100, label="password", widget=forms.PasswordInput())
    
    