import os
from datetime import datetime, timedelta

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import DetailView, FormView, TemplateView
from django.views.generic.edit import CreateView

from rest_framework.response import Response
from rest_framework.views import APIView
from toothpaste.forms import DocumentForm
from toothpaste.models import DocumentModel
from toothpaste.text_processor.processor import FrequencyDistributor


class IndexView(FormView, CreateView):
    template_name = 'toothpaste/home.html'
    form_class = DocumentForm
    FrequencyDistributor = FrequencyDistributor()

    def get_success_url(self):
        document = self.object
        return reverse(
            'result-detail', args=[
                document.uid,
            ])

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


class ResultView(DetailView, FrequencyDistributor):
    template_name = 'toothpaste/result.html'
    model = DocumentModel
    queryset = model.objects.all()

    def get_queryset(self, **kwargs):
        return self.queryset.filter(
            date__gte=datetime.now() - timedelta(days=1))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uid'] = self.object.uid
        return context


class ChartData(APIView, DetailView, FrequencyDistributor):
    authentication_classes = []
    permission_classes = []
    FrequencyDistributor = FrequencyDistributor()
    model = DocumentModel

    def get(self, request, pk, format=None):
        self.object = self.get_object()
        document = self.object.document.path
        f = self.FrequencyDistributor.text_extractor_filter(document)
        f = self.FrequencyDistributor.process(f)
        words = f[0]
        freqs = f[1]
        data = {
            'words': words,
            'freqs': freqs,
        }
        return Response(data)
