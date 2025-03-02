from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import date
from .models import Post, Author, Tag
import sys


all_posts = [
]


def get_date(post_data):
    return post_data['date']

# Create your views here.


# def index(request):
#     sorted_posts = sorted(all_posts, key=get_date)
#     latest_posts = sorted_posts[-3:]
#     return render(request, 'blog/index.html', {
#         "posts": latest_posts
#     })

def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
        "posts": all_posts
    })


def full_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/full-post.html', {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
