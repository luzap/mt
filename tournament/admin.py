from django.contrib import admin
from .models import School, Individual, Post, Language


class SchoolAdmin(admin.ModelAdmin):
    """Creates a custom view for the School table. This includes editing and display."""
    model = School
    list_display = ('name', 'code')  # These two values will be shown when viewing
    readonly_fields = ('code',)  # Does not allow editing in admin page. Done for the purpose of autogen


class IndividualAdmin(admin.ModelAdmin):
    """Creates a custom Individual admin view."""
    model = Individual
    list_display = ('name', 'surname', 'email', 'school')


class PostAdmin(admin.ModelAdmin):
    """Creates a custom Post admin view."""
    model = Post
    list_display = ('title', 'date_published', 'author', 'body')


admin.site.register(School, SchoolAdmin)  # The view is registered with the data type
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Language)  # Default views can be used as well
admin.site.register(Post, PostAdmin)
