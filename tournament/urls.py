from django.conf.urls import url

from . import views

handler404 = 'tournament.views.handler404'

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^registration/', views.registration, name='registration'),
]
