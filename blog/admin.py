from django.contrib import admin
from django.db import models

from blog.models import Category, Nibble, Post, NibbleCategory


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "last_modified")
    list_filter = ("status",)
    search_fields = ["title"]


class NibbleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Nibble, NibbleAdmin)
admin.site.register(NibbleCategory, NibbleAdmin)