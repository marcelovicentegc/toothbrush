from django.db import models
from django.utils import timezone
from .validators import validate_file_type, validate_file_size
from django.core.files.storage import FileSystemStorage
from django.urls import reverse



class DocumentModel(models.Model):
    document = models.FileField(upload_to='documents', null=False, blank=False, default='default', validators=[validate_file_type, validate_file_size], max_length=255)
    date = models.DateTimeField(default=timezone.now)
    # processed = models.TextField(default='')
    # expires = models.DateTimeField(default='test')
    # url_hash = models.CharField(blank=False, max_length=32, unique=True, default='test')

    def get_absolute_url(self):
        return reverse('result-detail', kwargs={'id': self.id})

    class Meta:
        verbose_name_plural: 'documents'