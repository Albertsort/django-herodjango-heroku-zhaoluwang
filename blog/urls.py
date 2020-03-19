from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:blog_id>', views.detail, name='detail'),
    path('comment/<int:post_id>', views.add_comment, name='add_comment'),
]
