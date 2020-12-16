from django.db import models
from markdownx.models import MarkdownxField


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        """Meta definition for Category."""
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = MarkdownxField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    read_time = models.IntegerField(default=0)
    like_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        """Meta definition for Post."""
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

# TODO: Comments
# class Comment(models.Model):
#     author = models.CharField(max_length=60)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)
