import os
from project.settings.base import MEDIA_ROOT
from django.test import TestCase, Client
from toothpaste.models import DocumentModel
from toothpaste.toilet_sink.soap import ToiletSink

path = os.path.join(MEDIA_ROOT, 'documents')

c = Client(enforce_csrf_checks=True)
c.get('/')
c.get('/about/')
with open(path + '/ESPN Case Study.docx', 'rb') as tf:
    c.post('/', {'document': tf}, follow=True)
with open(path + '/Renewable Energy Statistics 2017.pdf', 'rb') as tf:
    c.post('/', {'document': tf}, follow=True)
with open(path + '/The Fox News Effect - Media Bias and Voting.pdf', 'rb') as tf:
    c.post('/', {'document': tf}, follow=True)

class ResultTestCase(TestCase):
    ToiletSink = ToiletSink()

    def setUp(self):
        DocumentModel.objects.create(document=('documents/ESPN Case Study.docx'))
        DocumentModel.objects.create(document=('documents/Renewable Energy Statistics 2017.pdf'))
        DocumentModel.objects.create(document=('documents/The Fox News Effect - Media Bias and Voting.pdf'))

    def test_flush(self):
        object_list = DocumentModel.objects.all()
        obj = object_list[0]
        obj1 = object_list[1]
        obj2 = object_list[2]
        document = obj.document.path
        document1 = obj1.document.path
        document2 = obj2.document.path

        f = self.ToiletSink.text_extractor(document)
        f1 = self.ToiletSink.text_extractor(document1)
        f2 = self.ToiletSink.text_extractor(document2)

        f = self.ToiletSink.final_cut(f)
        f1 = self.ToiletSink.final_cut(f1)
        f2 = self.ToiletSink.final_cut(f2)


