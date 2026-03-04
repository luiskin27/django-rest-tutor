from django.contrib import admin
from .models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner_username', 'created', 'language')
    list_filter = ('language', 'style')
    search_fields = ('title', 'code')

    def owner_username(self, obj):
        return obj.owner.username if obj.owner else '-'
    
    owner_username.short_description = 'Owner'