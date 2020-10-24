from django.contrib import admin
from .models import Post, PostView, Comment, Love, User

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Love)