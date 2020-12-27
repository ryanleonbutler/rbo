from django.views.generic import ListView, DetailView
from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "posts.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "post.html"
