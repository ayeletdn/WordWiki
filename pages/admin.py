from django.contrib import admin
from pages.models import Page, Comment


class PageAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'short_definition', 'comments_count')
    search_fields = ['display_name', 'definition']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'page')

admin.site.register(Page, PageAdmin)
admin.site.register(Comment, CommentAdmin)