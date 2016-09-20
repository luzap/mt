from django.shortcuts import render, render_to_response, redirect

from tournament.forms import CodeForm, RegistrationForm
from .models import School, Post


def handler404(request):
    """Custom 404 error handler."""
    response = render_to_response('404.html', {})
    response.status_code = 404  # Other errors can be similarly configured
    return response


def index(request):
    """Renders index page."""
    return render(request, 'index.html')


# TODO Make pages this function refers to
def get_school_code(request):
    if request.method == "POST":
        form = CodeForm(request.POST)  # This populates the local from with data from the form
        # Checks for form validity and whether or not the code exists.
        if form.is_valid() and (School.objects.filter(code=form.cleaned_data['code']).count() != 0):
            code = form.cleaned_data['code']  # Data is returned in form of dictionary
            registration(request, code=code)  # Redirect to individual registration page
        else:
            return redirect("error.html", {'reason': "School does not exist. Please check with your coordinator."})
    else:
        form = CodeForm()  # Creates a blank form
        return render(request, 'code.html', {'form': form})  # Renders the blank form onto the page


def registration(request, code=None):
    """Displays the registration form and adds it to database."""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("confirm.html")
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form, 'code': code})


def read_article(request, post_id):
    """Returns post """
    post = Post.objects.filter(id=post_id)  # Data retrieved via post_id
    return render("post.html", {"post": post})
