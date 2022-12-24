from django.shortcuts import render
from .models import Post
# Create your views here.

def blog_main(request, *args):
    data_dict  ={
        "posts": Post.objects.all()
    }
    return render(request, 'blog_main.html', data_dict)

def slug_process(request, slug):
    post_slugs = [ p.post_slug for p in Post.objects.all()]
    if slug in post_slugs:
        post = Post.objects.get(post_slug = slug)
        data_dict = { 'post': post }
        return render(request, 'post_view.html', data_dict)