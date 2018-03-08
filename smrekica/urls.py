from django.conf.urls import url
from . import views

# na tem naslovu kliči views.index

urlpatterns = [
    url(r'^$', views.index, name = 'smrekica'),
]
