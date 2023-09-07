""" Views de posts """
# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View

# Views
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm, CommentForm

# Models
from posts.models import Posts, Comment


class PostsFeedView(LoginRequiredMixin, ListView):
    """Returna todos los posts publicados"""

    template_name = "posts/feed.html"
    model = Posts
    ordering = "-created"
    paginate_by = 4
    context_object_name = "posts"


class PostDetailView(LoginRequiredMixin, DetailView):
    """Vista para los detalles del post"""

    template_name = "posts/details.html"
    queryset = Posts.objects.all()
    context_object_name = "post"
    slug_field = "pk"
    slug_url_kwarg = "id_post"


class CreateCommentView(LoginRequiredMixin, CreateView):
    """Vita para crear los comentarios"""
    
    template_name = "posts/details.html"
    form_class = CommentForm
    # success_url = reverse_lazy("posts:feed")

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.get_object(Posts.objects.all().pk)})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context


class PostCommentView(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        view = CreateCommentView.as_view()
        return view(request, *args, **kwargs)

class CreatePostView(LoginRequiredMixin, CreateView):
    """Vita para crear los posts"""

    template_name = "posts/new.html"
    form_class = PostForm
    success_url = reverse_lazy("posts:feed")

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context

def postLikeView(request, post_id):
    """Vista para dar like a un post"""
    post = get_object_or_404(Posts, pk=post_id)
    user = request.user.profile
    post.likes.add(user)
    return redirect(reverse("posts:detail", kwargs={"id_post": post.pk}))

def postUnlikeView(request, post_id):
    """Vista para quitar el like a un post"""
    post = get_object_or_404(Posts, pk=post_id)
    user = request.user.profile
    post.likes.remove(user)
    return redirect(reverse("posts:detail", kwargs={"id_post": post.pk}))

def commentLikeView(request, comment_id):
    """Vista para dar like a un post"""
    comment = get_object_or_404(Comment, pk=comment_id)
    user = request.user.profile
    post = comment.post
    comment.likes.add(user)
    return redirect(reverse("posts:detail", kwargs={"id_post": post.pk}))

def commentUnlikeView(request, comment_id):
    """Vista para quitar el like a un post"""
    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    user = request.user.profile
    comment.likes.remove(user)
    return redirect(reverse("posts:detail", kwargs={"id_post": post.pk}))

