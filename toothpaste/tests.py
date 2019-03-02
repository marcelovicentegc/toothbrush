import os

from django.test import Client, TestCase

from project.settings.base import MEDIA_ROOT
from toothpaste.models import DocumentModel
from toothpaste.text_processor.processor import FrequencyDistributor

path = os.path.join(MEDIA_ROOT, 'documents')

c = Client(enforce_csrf_checks=True)
c.get('/')
c.get('/about/')
with open(path + '/ESPN Case Study.docx', 'rb') as tf:
    c.post('/', {'document': tf}, follow=True)
with open(path + '/Renewable Energy Statistics 2017.pdf', 'rb') as tf:
    c.post('/', {'document': tf}, follow=True)
with open(path + '/The Fox News Effect - Media Bias and Voting.pdf',
          'rb') as tf:
    c.post('/', {'document': tf}, follow=True)


class ResultTestCase(TestCase):
    FrequencyDistributor = FrequencyDistributor()

    def setUp(self):
        DocumentModel.objects.create(
            document=('documents/ESPN Case Study.docx'))
        DocumentModel.objects.create(
            document=('documents/Renewable Energy Statistics 2017.pdf'))
        DocumentModel.objects.create(
            document=(
                'documents/The Fox News Effect - Media Bias and Voting.pdf'))

    def test_(self):
        object_list = DocumentModel.objects.all()
        obj = object_list[0]
        obj1 = object_list[1]
        obj2 = object_list[2]
        document = obj.document.path
        document1 = obj1.document.path
        document2 = obj2.document.path

        f = self.FrequencyDistributor.text_extractor_filter(document)
        f1 = self.FrequencyDistributor.text_extractor_filter(document1)
        f2 = self.FrequencyDistributor.text_extractor_filter(document2)

        f = self.FrequencyDistributor.process(f)
        f1 = self.FrequencyDistributor.process(f1)
        f2 = self.FrequencyDistributor.process(f2)
