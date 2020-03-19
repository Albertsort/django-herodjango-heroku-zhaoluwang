from django.contrib import admin

from .models import Article
from .models import Comment

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'modified_time', 'author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'post', 'created_time']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
