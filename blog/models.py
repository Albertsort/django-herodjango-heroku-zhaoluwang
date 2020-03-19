from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, verbose_name='文章标题')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=140, verbose_name='评论内容')
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_time', )

    def __str__(self):
        return self.comment[:20]


