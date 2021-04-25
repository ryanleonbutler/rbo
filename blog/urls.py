from django.conf.urls import url
from django.urls import path
from blog.views import PostDetailView, IndexListView, BlogListView
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url("blog", BlogListView.as_view(), name="posts"),
    url("contact", views.page_contact, name="contact"),
    url("about", views.page_about, name="page"),
    url("yandex_fd81df80c0db7580.html", views.yandex, name="yandex"),
    url("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    url('search', views.post_search, name='search_results'),
    path("<slug:slug>", PostDetailView.as_view(), name="post"),
    path("<category>", views.post_category, name="post_category"),
    url("", IndexListView.as_view(), name="posts"),
]
