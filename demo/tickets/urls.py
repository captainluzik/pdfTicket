from django.conf.urls import include, url
from django.contrib import admin
from .views import GeneratePdf


urlpatterns = [
    url(r'^pdf/(?P<user_id>[0-9]+)/$', GeneratePdf.as_view(), name='generatepdf'),
]