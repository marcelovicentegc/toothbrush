import os
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, FormView, DetailView
from django.views.generic.edit import CreateView
from toothpaste.forms import DocumentForm
from toothpaste.models import DocumentModel
from toothpaste.toilet_sink.soap import ToiletSink
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings




class IndexView(FormView, CreateView):
    template_name = 'toothpaste/home.html'
    form_class = DocumentForm
    ToiletSink = ToiletSink()

    def get_success_url(self):
        document = self.object
        return reverse('result-detail', args=[document.id])

    def form_valid(self, form):
        form.save()
        return super(IndexView, self).form_valid(form)

    def upload_file(self, request):
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                document = form.cleaned_data['document']
                document.save(commit=True)
                return redirect(self.get_success_url())
        else: 
            form = DocumentForm()
        return render(request, self.template_name, {'form': form})





class AboutView(TemplateView):
    template_name = 'toothpaste/about.html'



# Temporary view
class ResultView(DetailView, ToiletSink):
    template_name = 'toothpaste/result.html'
    model = DocumentModel
    ToiletSink = ToiletSink()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Process file!
        # e = []
        # for i in self.object.document:
        #     e.append(i)
        # e = str(e)
        document = self.object.document.path
        f = self.ToiletSink.text_extractor(document)
        f = self.ToiletSink.final_cut(f)
        context['words'] = f[0]
        context['freqs'] = f[1]
        context['id'] = self.object.id
        data = {
            'words': context['words'],
            'freq': context['freqs'],
            'id': context['id'],
        }
        return data




    # document = model.id
    # def surgery(file):
    #   file.open('r')
    #   for i in file:
    #         print(i)
    #   file.close()
    # for i in document.document:
    #     with open(os.path.join(settings.MEDIA_ROOT, 'documents/tabula_rasa.txt'), 'w') as f:
    #         body = self.ToiletSink.text_extractor(i)
    #         head = self.ToiletSink.final_cut(body)
    #         f.write(head)
    # # path = os.path.join(settings.MEDIA_ROOT, 'documents/')
    # with open('tabula_rasa.txt', 'w') as f:
    #     body = self.ToiletSink.text_extractor(document)
    #     head = self.ToiletSink.final_cut(body)
    #     f.write(head)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['document'] = self.queryset
    #     return context




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