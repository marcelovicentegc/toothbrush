from django.db import models
from django.utils import timezone
from project.validators import validate_file_type




class DocumentModel(models.Model):
    #document = models.TextField(blank=False)
    document = models.FileField(upload_to='documents', null=True, blank=True, max_length=255, validators=[validate_file_type])
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural: 'documents'