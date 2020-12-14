from django.contrib import admin
from .models import Thread, Comment

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('topic', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['topic', 'description']
    prepopulated_fields = {'slug': ('topic',)}


admin.site.register(Thread, ThreadAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'thread', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
