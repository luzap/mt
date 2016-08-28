from django.shortcuts import render, render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def index(request):
    pass


def registration(request):
    return render()


def read_article(request):
    pass
