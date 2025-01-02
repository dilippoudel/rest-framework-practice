"""Django admin site for snippets."""
from django.contrib import admin

from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    """Define the snippet pages."""
    ordering = ['id']
    list_display = ['title', 'language', 'created']

admin.site.register(Snippet, SnippetAdmin)
