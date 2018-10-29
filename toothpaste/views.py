from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, DetailView
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

    def create_document(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)

            if form.is_valid():
                form.save(commit=True)
                return redirect(self.success_url)
            else: 
                form = DocumentForm()
    
        return render(request, self.template_name, {'form': form})





class AboutView(TemplateView):
    template_name = 'toothpaste/about.html'




class ResultView(TemplateView):
    template_name = 'toothpaste/result.html'




class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        words = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'] # DocumentModel.objects.filter()
        freq = [12, 21, 42, 13, 9, 19]
        data = {
            'words': words,
            'freq': freq,
        }
        return Response(data)