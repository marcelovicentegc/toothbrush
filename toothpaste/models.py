from django.db import models
from django.utils import timezone
from .validators import validate_file_type, validate_file_size
from django.core.files.storage import FileSystemStorage



class DocumentModel(models.Model):
    document = models.FileField(upload_to='documents', null=False, blank=False, default='default', validators=[validate_file_type, validate_file_size], max_length=255)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural: 'documents'