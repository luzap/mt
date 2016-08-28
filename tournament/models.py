from django.db import models
from . import utils
# Create your models here.


# TODO Add query for number of competitors
class School(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    code = models.CharField(max_length=7)

    class Meta:
        pass


class Language(models.Model):
    language = models.CharField(max_length=15)

    class Meta:
        pass


class Individual(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    school = models.ForeignKey(School)
    email = models.EmailField(blank=False)
    languages = models.ForeignKey(Language)

    class Meta:
        pass




