from django.shortcuts import render
from .models import Post


def blog_main(request, *args):
    posts = Post.objects.all()
    data_dict = {
        "posts": posts
    }
    return render(request, 'blog_main.html', data_dict)