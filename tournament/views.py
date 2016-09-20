from django.shortcuts import render, render_to_response, redirect

from tournament.forms import CodeForm, RegistrationForm
from .models import School, Post


def handler404(request):
    """Custom 404 error handler."""
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def index(request):
    """Renders index page."""
    return render(request, 'index.html')

def register(request):
    """Renders registration page."""
    return render(request, 'registration.html')


# TODO Make pages this function refers to
def get_school_code(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        # Checks for form validity and whether or not the code exists.
        if form.is_valid() and (School.objects.filter(code=form.cleaned_data['code']).count() != 0):
            code = form.cleaned_data['code']
            addmember(request, code=code)
        else:
            return redirect("error.html", {'reason': "School does not exist. Please check with your coordinator."})
    else:
        form = CodeForm()
        return render(request, 'code.html', {'form': form})


# TODO Make sure if code=NONE, don't render anything
def addmember(request, code=None):
    """Displays the registration form and adds it to database."""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("confirm.html")
    else:
        form = RegistrationForm()
        return render(request, 'addmember.html', {'form': form, 'code': code})


def read_article(request, post_id):
    """Returns post """
    post = Post.objects.filter(id=post_id)
    return render("post.html", {"post": post})
