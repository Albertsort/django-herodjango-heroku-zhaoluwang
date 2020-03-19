from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import Article
from .models import Comment
from .form import CommentForm

# Create your views here.

def rredirect(request, post):
    form = CommentForm()
    comment_list = post.comment_set.all()
    return render(request, 'blog/detail.html', {'object': post,
                                                'form': form,
                                                'comment_list': comment_list})


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Article.objects.all()


def detail(request, blog_id):
    post = get_object_or_404(Article, pk=blog_id)
    form = CommentForm()
    comment_list = post.comment_set.all()
    return render(request, 'blog/detail.html', {'object': post,
                                                'form': form,
                                                'comment_list': comment_list})
    

def add_comment(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return rredirect(request, post)
        else:
            rredirect(request, post)
    return rredirect(request, post)



# class DetailView(generic.DetailView):
#     model = Article
#     template_name = 'blog/detail.html'