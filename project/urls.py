from django.contrib import admin
from django.urls import re_path, include
from django.views.static import serve
from project import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('toothpaste.urls')),
]

if settings.dev.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.dev.MEDIA_ROOT,
        }),
    ]
