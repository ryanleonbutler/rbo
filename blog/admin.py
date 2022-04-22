from django.contrib import admin
from django.contrib.sites.models import Site
from django.db import models

from blog.models import Post, Tag


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "last_modified")
    list_filter = ("status",)
    search_fields = ["title"]


class NibbleAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Site)


class SiteAdmin(admin.ModelAdmin):
    fields = ("id", "name", "domain")
    readonly_fields = ("id",)
    list_display = ("id", "name", "domain")
    list_display_links = ("name",)
    search_fields = ("name", "domain")


admin.site.register(Site, SiteAdmin)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, CategoryAdmin)
