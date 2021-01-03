from django.views.generic import ListView, DetailView
from django.shortcuts import render
from blog.models import Post
from tracking_analyzer.models import Tracker
from hitcount.views import HitCountDetailView


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name = "post_list"
    template_name = "posts.html"

    def get_object(self, queryset=None):
        # Retrieve the blog post just using `get_object` functionality.
        obj = super(PostListView, self).get_object(queryset)

        # Track the users access to the blog by post!
        Tracker.objects.create_from_request(self.request, obj)

        return obj


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    context_object_name = "post_detail"
    template_name = "post.html"

    def get_object(self, queryset=None):
        # Retrieve the blog post just using `get_object` functionality.
        obj = super(PostDetailView, self).get_object(queryset)

        # Track the users access to the blog by post!
        Tracker.objects.create_from_request(self.request, obj)

        return obj


def post_category(request, category):
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


def page_about(request):
    return render(request, "about.html")


def page_contact(request):
    return render(request, "contact.html")
