from django import forms
from .models import Page

class NewWikiPage(forms.ModelForm):
    class Meta:
        model = Page