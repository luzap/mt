import django
from django.db import models
from . import utils


# TODO Add query for number of competitors
class School(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    code = models.CharField(max_length=10)

    def __init__(self):
        self.code = utils.gen_code(self.name)


    def __repr__(self):
        return self.name

    class Meta:
        pass


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=15, default=" ")

    def __repr__(self):
        return self.language

    class Meta:
        pass


class Individual(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    school = models.ForeignKey(School)
    email = models.EmailField(blank=False)

    def __repr__(self):
        return "{} {}".format(self.name, self.surname)

    class Meta:
        pass


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateField(default=django.utils.timezone.now)

    def __repr__(self):
        return self.title





