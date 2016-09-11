"""
A single Django site is made to allow multiple apps. This is the top level URL matcher, where each of the
regular expression strings is matched against the input typed into the user's browser.
"""


from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

# TODO Make custom error pages (405, et cetera)
handler404 = 'tournament.views.handler404'  # Enables having custom 404 pages
urlpatterns = [
    url(r'^admin/', admin.site.urls),  # Highest level view for the administrator of the site
    url(r'^tournament/', include('tournament.urls'))  # At this point, refers to tournament/urls.py
]
