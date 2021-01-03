from django.conf.urls import url
from django.urls import path
from blog.views import PostDetailView, PostListView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    url("contact/", views.page_contact, name="contact"),
    url("about/", views.page_about, name="page"),
    path("<slug:slug>", PostDetailView.as_view(), name="post"),
    path("<category>/", views.post_category, name="post_category"),
]
