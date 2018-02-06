from django import forms
from django.db import models
from .models import CsgoGif, OWGif

class CsgoGifForm(forms.ModelForm):
    class Meta:
        model = CsgoGif
        fields = ('title', 'image', 'description', 'weapon_used')
        widgets = {
            'weapon_used': forms.Select(attrs={'class': 'form-control'})
        }
        
class OWGifForm(forms.ModelForm):
    class Meta:
        model = OWGif
        fields = ('title', 'image', 'description', 'hero_class')
        widgets = {
            'hero_class': forms.Select(attrs={'class': 'form-control'})
        }
        
class CsgoGifFilter(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    weapon = forms.ChoiceField(choices=CsgoGif.WEAPONS)

class OWGifFilter(forms.ModelForm):    
    title = forms.CharField(max_length=100, required=False)
    hero = forms.ChoiceField(choices=OWGif.HEROES)
