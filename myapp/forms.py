from django import forms
from .models import Mymodel

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Mymodel
        fields = ['title', 'file']  # Указываем, какие поля будем использовать
