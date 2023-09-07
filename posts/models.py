"""Modelos de posts"""

# Django
from django.db import models
from django.contrib.auth.models import User
from users import models as usr

# from users.models import Profile


class Posts(models.Model):
    """Posts de models"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/photos")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        usr.Profile,
        verbose_name="like",
        related_name="post_likes",
    )

    def __str__(self):
        """Return title and username"""
        return f"{self.title} by @{self.user.username}"


class Comment(models.Model):

    text = models.TextField(max_length=255)
    post = models.ForeignKey(
        Posts, verbose_name="post comment", on_delete=models.CASCADE, null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(
        usr.Profile, verbose_name="user comment", on_delete=models.CASCADE
    )

    likes = models.ManyToManyField(
        usr.Profile,
        verbose_name="like",
        related_name="comment_likes",
    )

    def __str__(self):
        """Return title and username"""
        return f"{self.text} by @{self.profile.user.username}"
