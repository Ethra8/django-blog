from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# Register your models here.
# noqa admin.site.register(Post) -- can be eliminated since we added class PostAdmin() with decorator @admin.register(Post)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommnentAdmin(SummernoteModelAdmin):
    list_display = ('post', 'body', 'author', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
