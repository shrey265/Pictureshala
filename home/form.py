from django import forms
from home.models import pictureModel

class PictureForm(forms.ModelForm):
    class Meta:
        model = pictureModel
        fields = ['story']