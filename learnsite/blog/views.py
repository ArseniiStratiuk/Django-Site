from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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

def register(request):
    # POST incoming
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get("username")
            messages.success(request, f"Створено новий акаунт: {username}")
            return redirect("/")
        else:
            print("ERROR DURING REGISTRATION!+")
            for msg in form.error_messages:
                messages.error(request, f"{msg}")
            return render(request, 'register.html', {'form': form})

    # GET incoming
    data_dict = {"form": UserCreationForm}
    return render(request, 'register.html', data_dict)

def logout_request(request):
    logout(request)
    messages.info(request, "Ви вийшли з акаунту")
    return redirect("/")

def login_request(request):
    for 