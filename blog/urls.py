from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path
from django.views.generic import TemplateView

from blog.models import NibbleCategory
from blog.views import (
    BlogListView,
    IndexListView,
    NibbleCategoryView,
    NibbleDetailView,
    NibbleListView,
    PostCategoryView,
    PostDetailView,
)

from . import views
from .sitemaps import NibbleSitemap, PostSitemap, StaticSitemap


sitemaps = {"blog": PostSitemap, "static": StaticSitemap, "py-nibbles": NibbleSitemap}

urlpatterns = [
    re_path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    re_path("contact/", views.page_contact, name="contact"),
    re_path("about/", views.page_about, name="about"),
    re_path("search/", views.post_search, name="search_results"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("blog/<slug:slug>", PostDetailView.as_view(), name="post"),
    path("blog/", BlogListView.as_view(), name="posts"),
    path("blog/category/<category>", PostCategoryView.as_view(), name="posts_category"),
    path("nibbles/<slug:slug>", NibbleDetailView.as_view(), name="nibble"),
    path("nibbles/", NibbleListView.as_view(), name="nibbles"),
    path("nibbles/category/<category>", NibbleCategoryView.as_view(), name="nibbles_category"),
    path("", IndexListView.as_view(), name="home"),
]

# handler504 = 'blog.views.error_504'
# handler502 = 'blog.views.error_502'
# handler500 = 'blog.views.error_500'
# handler404 = 'blog.views.error_404'
# handler403 = 'blog.views.error403'
# handler400 = 'blog.views.error400'
