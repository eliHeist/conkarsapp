from django.shortcuts import render
from django.views.generic import ListView, DetailView

from posts.models import Article

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "posts/post-list.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "posts/post-detail.html"
    context_object_name = "article"

