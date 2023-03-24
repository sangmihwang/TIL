from django import forms
from .models import Movie
from django.forms.widgets import DateInput, NumberInput


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'score': forms.NumberInput(attrs={'step': 0.5, 'type': 'number'})
        }
    