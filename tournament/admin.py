from django.contrib import admin
from .models import School, Individual, Post, Language


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'email')


class IndividualAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'author', 'body')


admin.site.register(School, SchoolAdmin)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Language)
admin.site.register(Post, PostAdmin)
