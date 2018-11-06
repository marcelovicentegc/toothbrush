import uuid
from django.db import models
from django.utils import timezone
from .validators import validate_file_type, validate_file_size
from django.urls import reverse
from django.http import request



class DocumentModel(models.Model):
    document = models.FileField(upload_to='documents', null=False, blank=False, default='default', validators=[validate_file_type, validate_file_size], max_length=255)
    date = models.DateTimeField(default=timezone.now)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_absolute_url(self):
        return reverse('result-detail', kwargs={'uid': self.uid})
        
    class Meta:
        verbose_name_plural: 'documents'