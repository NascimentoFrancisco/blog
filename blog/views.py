from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from blog.models import Posts


class ListPostsView(ListView):
    model = Posts
    template_name = "list.html"
    context_object_name = "posts"
    paginate_by = 10


class DetailPostView(DetailView):
    model = Posts
    template_name = 'detail.html'
    context_object_name = 'post'
