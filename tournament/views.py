from django.shortcuts import render, render_to_response, redirect

from tournament.forms import CodeForm


def handler404(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def index(request):
    return render(request, 'index.html')


def school(request):
    form = CodeForm()


def registration(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("confirm.html")
    else:
        form = CodeForm()
        return render(request, 'registration.html', {'form': form})


def read_article(request):
    pass

