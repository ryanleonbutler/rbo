from django.urls import path
from blog.views import PostDetailView, PostListView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("<slug:slug>", PostDetailView.as_view(), name="post"),
    path("<category>/", views.blog_category, name="blog_category"),
]
