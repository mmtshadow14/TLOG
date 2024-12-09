from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from home.models import Post, LikeRelation, CommentsModel, PicOfTheSite
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeView(View):
    def get(self, request):
        topLogo = PicOfTheSite.objects.get(imageName='top logo of the site')
        navbarLogo = PicOfTheSite.objects.get(imageName='navbar logo')
        posts = Post.objects.all()
        return render(request, 'home/home.html', {'posts': posts, 'topLogo': topLogo, 'navbarLogo': navbarLogo})

class PostDetailView(View):
    template_name = 'home/postDetail.html'
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        like = LikeRelation.objects.filter(postLikedId=pk).count()
        comments = CommentsModel.objects.filter(commentOnPost=pk)
        return render(request, self.template_name, {'post': post, 'like': like, 'comments': comments})


class ProfileView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        userPosts = Post.objects.filter(author=user.username)
        return render(request, 'home/profileView.html', {'user': user, 'userPosts': userPosts})


class CreatePostView(LoginRequiredMixin, View):
    form_class = forms.PostCreateForm
    template_name = 'home/postCreate.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Post.objects.create(author=request.user.username, picture=cd['picture'], title=cd['title'], content=cd['content'])
            messages.success(request, 'Your post has been created!')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class LikePostView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        is_exists = LikeRelation.objects.filter(postLikedId=post_id, postLikedBy=request.user.username)
        if is_exists is None:
            messages.error(request, 'You have already liked this post!')
            return redirect('home:postDetail', pk=post_id)
        else:
            LikeRelation.objects.create(postLikedId=post_id, postLikedBy=request.user.username)
            messages.success(request, 'You liked this post!')
            return redirect('home:postDetail', pk=post_id)


class CommentView(LoginRequiredMixin, View):
    form_class = forms.CommentForm
    template_name = 'home/comment.html'
    def get(self, request, post_id):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, post_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            CommentsModel.objects.create(commentAuthor=request.user.username, commentOnPost=post_id, comment=cd['comment'])
            messages.success(request, 'Your comment has been posted!')
            return redirect('home:postDetail', pk=post_id)
        else:
            messages.error(request, 's.th went wrong!')
            return redirect('home:postDetail', pk=post_id)
































