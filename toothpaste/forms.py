from django import forms
from django.forms import ModelForm
from toothpaste.models import DocumentModel




class DocumentForm(ModelForm):
    document = forms.FileField(label='')

    class Meta:
        model = DocumentModel
        fields = ['document']
        