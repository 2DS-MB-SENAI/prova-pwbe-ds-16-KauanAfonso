from django import form
from .models import *

class FormConsulta(form.Form):
    class Meta:
        model = Client
        fields = '__all__'

    