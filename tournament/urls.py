from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatters = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.index, name='home')
]