from django.contrib import admin
from posts.models import Posts
# Register your models here.


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    """Registro de posts en admin """

    list_display = ("pk","user","title","photo","profile","created")
    list_editable = ("user","profile")
    list_display_links = ("pk","title")

    search_fields = ("user","profile","title","created","modified")

    list_filter = ("created",)