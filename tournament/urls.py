from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^registration/', views.registration, name='registration'),
    url(r'^404/', views.handler404, name='404')
]