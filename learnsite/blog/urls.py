from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.blog_main), # domen.com/blog/
    path('register/', views.register),
    path('logout/', views.logout_request),
    path('<slug>/', views.slug_process),
]