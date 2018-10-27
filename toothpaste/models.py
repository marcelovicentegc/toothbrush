from django.db import models
from django.utils import timezone




class DocumentModel(models.Model):
    #document = models.TextField(blank=False)
    document = models.FileField(upload_to='documents', null=True, blank=True, max_length=255)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural: 'documents'