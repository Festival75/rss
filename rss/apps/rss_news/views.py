from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rss.apps.rss_news.models import Post
from rss.apps.rss_news.models import User


def index(request):
    posts = reversed(Post.objects.all())
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def post(request, id):
    try:
        post = Post.objects.get(id=id)
        previous_id = post.id - 1
        next_id = post.id + 1
        context = {
            'post': post,
            'previous_id': previous_id,
            'next_id': next_id,
            'max_id': len(Post.objects.all())
        }
        return render(request, 'post.html', context)
    except Post.DoesNotExist:
        return render(request, 'error.html')


def signup_user(request):
    username = request.POST['username']
    password = request.POST['password']
    password_repeat = request.POST['password_repeat']
    email = request.POST['email']
    id = len(User.objects.all()) + 1
    new_user = User(id=id, username=username, password=password, email=email)
    new_user.save()
    return HttpResponseRedirect('/')

def check_username(request):
    if request.GET:
        username = request.GET['username']
        names = set([user.username for user in User.objects.all()])
        if username in names:
            return HttpResponse('no', content_type='text/html')
        else:
            return HttpResponse('yes', content_type='text/html')
    else:
        pass
