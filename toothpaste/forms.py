from django import forms
from django.forms import ModelForm
from toothpaste.models import DocumentModel
from project.validators import validate_file_type




class DocumentForm(ModelForm):
    document = forms.FileField(max_length=255, required=True, label='', validators=[validate_file_type])

    class Meta:
        model = DocumentModel
        fields = ['document']
        
        