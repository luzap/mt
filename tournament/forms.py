from django import forms

from .models import School, Individual


class CodeForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('code',)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ('name', 'surname', 'languages')
