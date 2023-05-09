from django import forms
from django.forms import ModelForm

from .models import *

class CoordinatesForm(forms.ModelForm):
    lat = models.CharField(max_length=3)
    lon = models.CharField(max_length=3)
    class Meta:
        model = Coordinates
        fields = '__all__'
