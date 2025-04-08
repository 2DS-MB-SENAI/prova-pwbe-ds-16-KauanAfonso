from django import forms
from .models import *

class FormConsulta(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    