from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Love, Comment
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'create'
        })
        return context
    
    
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'update'
        })
        return context
    


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


def love(request, slug):
    post = get_object_or_404(Post, slug=slug)
    love_qs = Love.objects.filter(user=request.user, post=post)
    if love_qs.exists():
        # unlike the post
        love_qs[0].delete()
        return redirect('detail', slug=slug)
    Love.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
