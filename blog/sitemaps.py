from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.publish_date

    def location(self, obj):
        return f"{obj.slug}"


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home', 'contact', "about"]

    def location(self, item):
        return reverse(item)
