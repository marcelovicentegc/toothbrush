from django import forms
from django.forms import ModelForm
from toothpaste.models import DocumentModel




class DocumentForm(ModelForm):
    document = forms.FileField(max_length=255, required=True, help_text="Files with accents in their names won't upload")

    class Meta:
        model = DocumentModel
        fields = ['document']
        
        