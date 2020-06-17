from django.conf.urls import url
from aban.views import note_soap_service

urlpatterns = [
    url(r'^api/epg/', note_soap_service),
]
