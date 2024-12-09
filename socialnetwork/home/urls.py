from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('postDetail/<int:pk>', views.PostDetailView.as_view(), name='postDetail'),
    path('profile/<int:user_id>', views.ProfileView.as_view(), name='profile'),
    path('createPost/', views.CreatePostView.as_view(), name='createPost'),
    path('like/<int:post_id>', views.LikePostView.as_view(), name='like'),
    path('comment/<int:post_id>', views.CommentView.as_view(), name='comment'),
]