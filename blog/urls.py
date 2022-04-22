from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path
from django.views.generic import TemplateView

from blog.views import IndexListView, PostDetailView, PostListView, TagsListView

from . import views
from .sitemaps import PostSitemap, StaticSitemap


sitemaps = {"blog": PostSitemap, "static": StaticSitemap}

urlpatterns = [
    re_path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    re_path("contact/", views.page_contact, name="contact"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("blog/<slug:slug>", PostDetailView.as_view(), name="post"),
    path("blog/posts/", PostListView.as_view(), name="posts"),
    path("blog/tags/<tag>", views.blog_tag, name="tag"),
    path("blog/tags/", TagsListView.as_view(), name="tags"),
    path("", IndexListView.as_view(), name="home"),
]
