from django.urls import re_path
from toothpaste.views import IndexView, AboutView, ResultView, ChartData



urlpatterns = [
    re_path(r'^$', IndexView.as_view()),
    re_path(r'^api/chart/data/(?P<pk>[\w-]+)/$', ChartData.as_view()),
    re_path(r'^result/(?P<pk>[\w-]+)/$', ResultView.as_view(), name='result-detail'),
    re_path(r'^about/$', AboutView.as_view()),
]