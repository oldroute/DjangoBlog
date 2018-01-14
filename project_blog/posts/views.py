from django.shortcuts import render
from .models import Post


def posts(request):
    posts = Post.objects.all()
    template = "posts/posts.html"
    context = {"posts": posts}
    return render(request, template, context)

