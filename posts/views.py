from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm


class PostsFeedView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/feed.html'


class PostsCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('posts:posts_feed')


class PostsUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('posts:posts_feed')


class PostsDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:posts_feed')
