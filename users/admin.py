""" User admin classes.
"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    # Los campos que se van a mostrar en el admin site profiles
    list_display = ("pk", "user", "website", "phone", "picture")
    # Los campos que son editables desde el menú
    list_editable = ("phone", "website", "picture")
    # Los campos que se pueden clickear para entrar a configurar el perfil
    list_display_links = ("pk", "user")

    # Los campos por los que se busca en la barra de busqueda
    search_fields = (
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
        "phone",
    )

    # Los campos que aparecen en el filtro de la derecha
    list_filter = ("user__is_active", "user__is_staff", "created", "modified")

    # Lo que se va a mostrar al abrir el menú pa editar
    # Una tuplas con tuplas, las tuplas interiores tienen el nombre de la sección
    # y un diccionario con los campos de esa sección, dicho diccionario recibe
    # una tupla de tuplas, cada elemento de la tupla va en una fila, si se quieren juntos
    # se ponen ambos en una tupla interior
    fieldsets = (
        (
            "Profile",
            {
                "fields": (("user", "picture"),),
            },
        ),
        (
            "Extra Info",
            {
                "fields": (
                    ("phone", "website"),
                    ("biography"),
                    ("follow"),
                )
            },
        ),
        ("Meta data", {"fields": (("created", "modified"),)}),
    )
    filter_horizontal = ("follow",)

    readonly_fields = ("created", "modified")


class ProfileInline(admin.StackedInline):
    """peofile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
