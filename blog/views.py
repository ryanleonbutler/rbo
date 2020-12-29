from django.views.generic import ListView, DetailView
from django.shortcuts import render
from blog.models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name = "post_list"
    template_name = "posts.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "post.html"


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "categories.html", context)
