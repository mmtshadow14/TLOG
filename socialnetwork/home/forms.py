from tokenize import Comment

from django import forms

from home.models import Post, CommentsModel


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['picture', 'title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ['comment']

        labels = {'comment': 'add your comment'}

