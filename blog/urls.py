from django.conf.urls import url
from django.urls import path
from blog.views import PostDetailView, IndexListView, BlogListView
from django.views.generic import TemplateView
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, StaticSitemap


sitemaps = {
    'blog': PostSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    url("yandex_fd81df80c0db7580.html", views.yandex, name="yandex"),
    url("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    url("blog/", BlogListView.as_view(), name="posts"),
    url("contact/", views.page_contact, name="contact"),
    url("about/", views.page_about, name="about"),
    url('search/', views.post_search, name='search_results'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path("<slug:slug>", PostDetailView.as_view(), name="post"),
    path("<slug:slug>", views.post_content, name="post"),
    path("<category>", views.post_category, name="post_category"),
    path("", IndexListView.as_view(), name="home"),
]
