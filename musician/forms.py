from . import models
from django import forms

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'
        widgets = {
            "instrument_type" : forms.CheckboxSelectMultiple(choices=[('rock', 'Rock'), ('classic', 'Classic'), ('pop', 'Pop')])
        }