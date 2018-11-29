# mysite/mysite/urls.py

from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^frame/', include('streaming.urls')),
    url(r'^upload/', include('uploading.urls')),
]
