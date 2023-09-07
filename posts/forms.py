# Django
from django import forms

# Models
from posts.models import Posts, Comment


class PostForm(forms.ModelForm):
    """Post model form"""

    class Meta:
        """Form settings"""

        model = Posts
        fields = ("user", "profile", "title", "photo")

class CommentForm(forms.ModelForm):
    """Comment model form"""

    class Meta:
        """Form settings"""

        model = Comment
        fields = ("profile", "text", "post")