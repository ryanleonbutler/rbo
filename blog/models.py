from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Publish"))


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        """Meta definition for Tag."""

        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="", max_length=200, editable=False)
    post_path = models.CharField(max_length=255, default="", blank=True)
    preview = models.CharField(max_length=255, default="", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    publish_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    tags = models.ManyToManyField("Tag", related_name="posts")
    read_time = models.IntegerField(default=0)
    like_counter = models.IntegerField(default=0, blank=True, editable=False)
    view_counter = models.IntegerField(default=0, blank=True, editable=False)
    author = models.CharField(max_length=255, default="Ryan", blank=False)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        """Meta definition for Post."""

        ordering = ["-publish_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
