from django import forms

from .models import School


class PostForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('code',)

