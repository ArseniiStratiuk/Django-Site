from django.shortcuts import render

def blog_main(request, *args):
    return render(request, 'blog_main.html', {})