from django.conf.urls import url
from django.urls import path
from blog.views import IndexListView, BlogListView, NibbleListView
from django.views.generic import TemplateView
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, StaticSitemap, NibbleSitemap


sitemaps = {
    'blog': PostSitemap,
    'static': StaticSitemap,
    'py-nibbles': NibbleSitemap
}

urlpatterns = [
    url("yandex_fd81df80c0db7580.html", views.yandex, name="yandex"),
    url("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    url("contact/", views.page_contact, name="contact"),
    url("about/", views.page_about, name="about"),
    url('search/', views.post_search, name='search_results'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("blog/<slug:slug>", views.post_content, name="post"),
    path("blog/", BlogListView.as_view(), name="posts"),
    path("blog/<category>", views.post_category, name="post_category"),
    path("nibbles/<slug:slug>", views.nibble_content, name="nibble"),
    path("nibbles/", NibbleListView.as_view(), name="nibbles"),
    path("", IndexListView.as_view(), name="home"),
]

# handler504 = 'blog.views.error_504'
# handler502 = 'blog.views.error_502'
# handler500 = 'blog.views.error_500'
# handler404 = 'blog.views.error_404'
# handler403 = 'blog.views.error403'
# handler400 = 'blog.views.error400'
