from django.http import HttpResponse
from django.shortcuts import render
from rss.apps.rss_news.models import Post


def index(request):
    posts = reversed(Post.objects.all())
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def post(request, id):
    try:
        post = Post.objects.get(id=id)
        result = post.text
    except Post.DoesNotExist:
        return HttpResponse('Post dose not exist')

    context = {
        'post': post,
    }
    return render(request, 'post.html', context)
