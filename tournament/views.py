from django.shortcuts import render, render_to_response

from tournament.forms import PostForm


def handler404(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def index(request):
    return render(request, 'index.html')


def registration(request):
    form = PostForm()
    return render(request, 'registration.html', {'form': form})


def read_article(request):
    pass

