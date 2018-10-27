from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from toothpaste.forms import DocumentForm
from toothpaste.models import DocumentModel
from toothpaste.toilet_sink.soap import ToiletSink
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response




class IndexView(FormView, ToiletSink):
    template_name = 'toothpaste/home.html'
    success_url = '/result/'
    form_class = DocumentForm

    def get(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                # f = " ".join(str(i) for i in file.document)
                # f = ToiletSink.preprocess(self, f)
                # f = ToiletSink.frequency_distribution(self, f, 20)
                # words = [i[0] for i in f]
                # freqs = [i[1] for i in f]
                # f_dict = {
                #           'word': words,
                #           'freq': freqs
                #           }
                # f = ToiletSink.jasonfy(self, f_dict)

                # form = form.cleaned_data['file']
                # return HttpResponseRedirect(self.success_url)
                return redirect(self.success_url)
        else:
            form = DocumentForm()
        return render(request, self.template_name, {'form': DocumentForm()})

class AboutView(TemplateView):
    template_name = 'toothpaste/about.html'


class ResultView(TemplateView):
    template_name = 'toothpaste/result.html'

    # def get(self, request, *args, **kwargs):
    #     try:
    #         obj = DocumentModel.objects.get(pk=1)
    #     except DocumentModel.DoesNotExist:
    #         raise Http404

    # def get(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         return render(request, self.template_name, {})
    #     else:
    #         return render(request, self.template_name, {})
    
    # def get_chart_data(self, request):
    #     document = DocumentModel.objects.filter()
    #     return render_to_response(self.template_name, {'document': document})

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