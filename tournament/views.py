from django.shortcuts import render, render_to_response, redirect
from django.core import mail

from .models import School
from tournament.forms import CodeForm, RegistrationForm


def handler404(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def index(request):
    return render(request, 'index.html')


def get_school_code(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid() and (School.objects.filter(code=form.cleaned_data['code']).count() != 0):
            code = form.cleaned_data['code']
            registration(request, code=code)
        else:
            return redirect("error.html")
    else:
        form = CodeForm()
        return render(request, 'code.html', {'form': form})


def registration(request, code=None):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("confirm.html")
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form, 'code': code})


def read_article(request, post_id):
    del post_id
    pass

