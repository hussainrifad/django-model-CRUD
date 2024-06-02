from django import forms
from . import models
from datetime import date

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'