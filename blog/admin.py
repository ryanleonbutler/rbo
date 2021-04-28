from django.db import models
from django.contrib import admin

from markdownx.widgets import AdminMarkdownxWidget

from blog.models import Post, Category, Nibble


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "last_modified")
    list_filter = ("status",)
    search_fields = ["title"]
    formfield_overrides = {
        models.TextField: {"widget": AdminMarkdownxWidget},
    }


class NibbleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "last_modified")
    list_filter = ("status",)
    search_fields = ["title"]
    formfield_overrides = {
        models.TextField: {"widget": AdminMarkdownxWidget},
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Nibble, NibbleAdmin)
