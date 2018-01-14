from django.shortcuts import render
from .models import Post


def posts(request):
    posts = Post.objects.all()
    template = "template.html"
    context = {"posts": posts}
    return render(request, template, context)

