"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path("", views.PostsFeedView.as_view(), name="feed"),
    path("posts/new", views.CreatePostView.as_view(), name="create"),
    path("posts/<int:id_post>", views.PostCommentView.as_view(), name="detail"),
    path("post/like/<int:post_id>", views.postLikeView, name="like_post"),
    path("comment/like/<int:comment_id>", views.commentLikeView, name="like_comment"),
]
