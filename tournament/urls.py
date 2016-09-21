from django.conf.urls import url

from . import views

handler404 = 'tournament.views.handler404'

urlpatterns = [
    url(r'^index/', views.index, name='index'),  # Main site, where all news and images will be displayed
    url(r'^register/', views.register, name='registration'),
    url(r'^code/', views.get_school_code, name='schoolcode'),
    url(r'^addmember/', views.addmember, name='addmember'),
    url(r'^memberlist/', views.memberlist, name='memberlist'),
]
