from django.contrib import admin
from .models import School, Individual, Post, Language


class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ('name',)
    readonly_fields = ('code',)


class IndividualAdmin(admin.ModelAdmin):
    model = Individual
    list_display = ('name', 'surname', 'email', 'school')


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'date_published', 'author', 'body')


admin.site.register(School, SchoolAdmin)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Language)
admin.site.register(Post, PostAdmin)
