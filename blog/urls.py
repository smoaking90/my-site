from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts-page'),
    path('post/<slug:slug>', views.full_post,
         name='full-post')  # posts/my-first-post
]
