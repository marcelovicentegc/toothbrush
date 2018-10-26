from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from toothpaste.forms import DocumentForm
from toothpaste.models import DocumentModel
from toothpaste.toilet_sink.soap import ToiletSink
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(TemplateView, ToiletSink):
    template_name = 'toothpaste/home.html'
    success_url = 'toothpaste/result.html'

    def get(self, request):
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form_prep = ToiletSink.preprocess(self, form)
                result = ToiletSink.frequency_distribution(self, form_prep, 5)
                result.save()
                return HttpResponseRedirect(self.success_url)
        else:
            form = DocumentForm()
            return render(request, self.template_name, {'form': form})


class AboutView(TemplateView):
    template_name = 'toothpaste/about.html'


class ResultView(TemplateView):
    template_name = 'toothpaste/result.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    
    #def get_chart_data(self, request):
     #   document = DocumentModel.objects.filter()
      #  return render_to_response(self.template_name, {'document': document})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        words = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
                # DocumentModel.obejcts.filter()
        freq = [12, 21, 42, 13, 9, 19]
        data = {
            'words': words,
            'freq': freq,
        }
        return Response(data)