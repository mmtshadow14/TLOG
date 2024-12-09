from datetime import timezone

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="posts/%Y/%m/%d")
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LikeRelation(models.Model):
    postLikedId = models.CharField(max_length=100)
    postLikedBy = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.postLikedId} liked by {self.postLikedBy}'



class CommentsModel(models.Model):
    commentAuthor = models.CharField(max_length=100)
    commentOnPost = models.CharField(max_length=100)
    comment = models.TextField()
    commentDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.commentAuthor} commented on {self.commentOnPost}'



class PicOfTheSite(models.Model):
    image = models.ImageField(upload_to="pics/%Y/%m/%d")
    imageName = models.CharField(max_length=100)
    def __str__(self):
        return self.imageName
