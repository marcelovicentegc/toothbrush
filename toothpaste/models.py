from django.db import models




class DocumentModel(models.Model):
    document = models.TextField(blank=False)

    class Meta:
        verbose_name_plural: 'documents'