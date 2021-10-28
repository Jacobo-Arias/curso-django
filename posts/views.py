""" Views de posts """
# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Views
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Posts


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
