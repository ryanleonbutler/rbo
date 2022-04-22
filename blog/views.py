from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Post, Tag
from blog.utils import get_post_content_from_file


class IndexListView(ListView):
    queryset = Post.objects.filter(status=1).order_by("-publish_date")
    template_name = "index.html"

    def get_object(self, queryset=None):
        return super(IndexListView, self).get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(status=1).order_by("-publish_date")
        return context


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by("-publish_date")
    context_object_name = "posts"
    template_name = "posts.html"

    def get_object(self, queryset=None):
        return super(PostListView, self).get_object(queryset)


class PostDetailView(DetailView):
    model = Post
    count_hit = True
    context_object_name = "post_detail"
    template_name = "post.html"

    def get_object(self, queryset=None):
        return super(PostDetailView, self).get_object(queryset)

    def get_context_data(self, **kwargs):
        obj = super(PostDetailView, self).get_object()
        context = super().get_context_data(**kwargs)
        context["content"] = get_post_content_from_file(obj.post_path)
        return context


class TagsListView(ListView):
    queryset = Tag.objects.all()
    context_object_name = "tags"
    template_name = "tags.html"

    def get_object(self, queryset=None):
        return super(PostListView, self).get_object(queryset)


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__name__contains=tag).order_by("-created_on")
    context = {"tag": tag, "posts": posts}
    return render(request, "tag.html", context)


def page_contact(request):
    return render(request, "contact.html")
