from django import forms
from django.forms import ModelForm
from toothpaste.models import DocumentModel




class DocumentForm(ModelForm):
    document = forms.FileField(max_length=255, required=True, label='')

    class Meta:
        model = DocumentModel
        fields = ['document']
        