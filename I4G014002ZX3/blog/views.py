from pyexpat import model
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Post
from django.views import generic

# Create your views here.

class PostListView (generic.ListView):
    model = Post
    # template_name = 'base.html'


class PostCreateView (generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView (generic.DetailView):
    model = Post

class PostUpdateView (generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView (generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


