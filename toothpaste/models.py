from django.db import models




class UniversityModel(models.Model):
    university = models.CharField(max_length=140, default='Test phase')
    course = models.CharField(max_length=140, default='Test phase')

    def __str__(self):
        return self.university

    class Meta:
        verbose_name_plural: 'universities'



class DocumentModel(models.Model):
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE)

    name = models.CharField(max_length=140, default='Test phase')
    email = models.EmailField(max_length=140, default='test@phase.com')
    document = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural: 'documents'