from django.contrib import admin
from rss.apps.rss_news.models import Post
from rss.apps.rss_news.models import User

# Register your models here.

admin.site.register(Post)
admin.site.register(User)
