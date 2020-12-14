from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, MarkdownModelAdmin)
admin.site.register(Category, CategoryAdmin)
