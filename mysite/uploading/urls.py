# mysite/uploading/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
        url(r'^upload_text/$', views.UploadTextView.as_view()),
        url(r'^upload_image/$', views.UploadImageView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
