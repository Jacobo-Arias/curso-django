from django.contrib import admin
from posts.models import Posts, Comment
from django.db.models import Count

# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ["text", "profile"]
    extra = 2


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    """Registro de posts en admin"""

    list_display = ("pk", "user", "title", "photo", "profile", "created", "comments")
    list_editable = ("user", "profile")
    list_display_links = ("pk", "title")

    search_fields = ("user", "profile", "title", "created", "modified")

    list_filter = ("created",)
    inlines = [CommentInline]

    def comments(self, obj):
        return obj.comments

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(comments=Count("comment"))
        return query


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("pk", "text", "post", "profile", "created")
    list_display_links = ("pk", "text")
    list_filter = ("post", "profile")
    search_fields = ("post", "text", "profile", "created")
