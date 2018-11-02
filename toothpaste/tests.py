from django.test import TestCase

# ResultView
from toothpaste.models import DocumentModel
from toothpaste.toilet_sink.soap import ToiletSink

ToiletSink = ToiletSink()
object_list = DocumentModel.objects.all()
# obj = object_list[0]
obj1 = object_list[23]
obj2 = object_list[21]
# document = obj.document.path
document1 = obj1.document.path
document2 = obj2.document.path

# f = ToiletSink.text_extractor(document)
f1 = ToiletSink.text_extractor(document1)
f2 = ToiletSink.text_extractor(document2)

# f = ToiletSink.final_cut(f)
f1 = ToiletSink.final_cut(f1)
f2 = ToiletSink.final_cut(f2)


