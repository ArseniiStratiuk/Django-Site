from django.urls import path, include, re_path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path(r'', views.PostListMain.as_view() ), # domen.com/blog/
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('logout/', views.logout_request),
    path('login/', views.login_request, name='login'),
    path('search_post/', views.PostListMain.as_view(), name="search"),
    path('profile/', views.profile, name='user_profile'),
    path('profile/<username>', views.look_profile, name='look_profile'),
    path('post_likes/<int:post_id>', views.like_post, name='like_post'),
    path('post/<slug:slug>/',views.ShowPost.as_view() , name="post_url"),
    path('post_saves/<int:post_id>', views.save_post, name='save_post'),
    path('saved_posts/', views.show_saved_post, name='saved_posts'),
    path('<slug>/', views.slug_process),
]