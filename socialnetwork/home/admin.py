from django.contrib import admin
from home.models import Post, LikeRelation, CommentsModel, PicOfTheSite

admin.site.register(Post)
admin.site.register(LikeRelation)
admin.site.register(CommentsModel)
admin.site.register(PicOfTheSite)
