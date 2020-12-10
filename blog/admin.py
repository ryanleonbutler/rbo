from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Category, CategoryAdmin)
