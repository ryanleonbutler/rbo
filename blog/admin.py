from django.db import models
from django.contrib import admin

from markdownx.widgets import AdminMarkdownxWidget

from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',
                    'status', 'created_on', 'last_modified')
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
