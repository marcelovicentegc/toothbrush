from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from toothpaste.forms import DocumentForm
from toothpaste.toilet_sink.soap import ToiletSink

class IndexView(TemplateView, ToiletSink):
    template_name = 'toothpaste/home.html'

    def get(self, request):
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form_prep = ToiletSink.preprocess(self, form)
                ToiletSink.lexical_diversity(self, form_prep)
                return HttpResponseRedirect('/result/')
        else:
            form = DocumentForm()
        
        return render(request, self.template_name, {'form': form})


class AboutView(TemplateView):
    template_name = 'toothpaste/about.html'


class ResultView(TemplateView):
    template_name = 'toothpaste/result.html'

