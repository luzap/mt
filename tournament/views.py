from django.shortcuts import render, render_to_response


def handler404(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def index(request):
    return render(request, 'index.html')


def registration(request):
    return render()


def read_article(request):
    pass
