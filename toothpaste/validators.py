import os
import magic
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError

def validate_file_type(upload):
        tmp_path = 'tmp/{}'.format(upload.name)
        default_storage.save(tmp_path, ContentFile(upload.file.read()))
        full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
        file_type = magic.from_file(full_tmp_path, mime=True)
        default_storage.delete(tmp_path)

        if file_type not in settings.DOCUMENT_TYPES:
                raise ValidationError('File type not supported. PDF, DOCX or TXT recommended.')

def validate_file_size(upload):
        if upload.size > settings.MAX_UPLOAD_SIZE:
                raise ValidationError('Please, keep file size under {} bytes. Current file size: {} bytes'.format(settings.MAX_UPLOAD_SIZE, upload.size))