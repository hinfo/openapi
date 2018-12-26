from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'^components/schemas/Contato$', ContatoList.as_view()),
    url(r'^components/schemas/ContatoCreate$', ContatoCreate.as_view()),
    url(r'^components/schemas/Contato/(?P<pk>[0-9]+)$', ContatoDetails.as_view()),
    url(r'^components/schemas/ContatoUpdate/(?P<pk>[0-9]+)$', ContatoUpdate.as_view()),
]
