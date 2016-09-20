from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class School(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    code = models.CharField(max_length=10)
    competitors = models.IntegerField(default=3)
    email = models.EmailField(default="example@email.com")

    @python_2_unicode_compatible
    def __str__(self):
        """String representation of the School model."""
        return self.name

    class Meta:
        """Meta class used for organization."""
        pass


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=15, default=" ")

    @python_2_unicode_compatible
    def __str__(self):
        return self.language

    class Meta:
        pass


class Individual(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    school = models.ForeignKey(School)
    email = models.EmailField(blank=False)

    @python_2_unicode_compatible
    def __str__(self):
        return "{} {}".format(self.name, self.surname)

    class Meta:
        pass


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateField(default=timezone.now)
    body = models.TextField()

    @python_2_unicode_compatible
    def __str__(self):
        return self.title

    class Meta:
        pass





