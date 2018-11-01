from django.urls import re_path
from toothpaste.views import IndexView, AboutView, ResultView, ChartData



urlpatterns = [
    re_path(r'^$', IndexView.as_view()),
    re_path(r'^api/chart/data/$', ChartData.as_view()),
    re_path(r'^result/(?P<pk>\d+)/$', ResultView.as_view(), name='result_detail'),
    re_path(r'^about/$', AboutView.as_view()),
]