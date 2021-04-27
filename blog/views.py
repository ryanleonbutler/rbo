from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from blog.models import Post
from tracking_analyzer.models import Tracker
from hitcount.views import HitCountDetailView
from blog.utils import get_post_content_from_file


class IndexListView(ListView):
    queryset = Post.objects.filter(status=1).order_by("-publish_date")
    context_object_name = "post_list"
    template_name = "index.html"

    def get_object(self, queryset=None):
        # Retrieve the blog post just using `get_object` functionality.
        obj = super(IndexListView, self).get_object(queryset)

        # Track the users access to the blog by post!
        Tracker.objects.create_from_request(self.request, obj)

        return obj


class BlogListView(ListView):
    queryset = Post.objects.filter(status=1).order_by("-publish_date")
    context_object_name = "post_list"
    template_name = "blog.html"

    def get_object(self, queryset=None):
        # Retrieve the blog post just using `get_object` functionality.
        obj = super(BlogListView, self).get_object(queryset)

        # Track the users access to the blog by post!
        Tracker.objects.create_from_request(self.request, obj)

        return obj


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    context_object_name = "post_detail"
    template_name = "postv2.html"

    def get_object(self, queryset=None):
        # Retrieve the blog post just using `get_object` functionality.
        obj = super(PostDetailView, self).get_object(queryset)
        print(obj.post_path)
        content = get_post_content_from_file(obj.post_path)
        print(content)

        # Track the users access to the blog by post!
        Tracker.objects.create_from_request(self.request, obj)

        return obj


def post_content(request, slug):
    post = Post.objects.get(slug=slug)
    content = get_post_content_from_file(post.post_path)

    context = {
        'post': post,
        'content': content
    }

    Tracker.objects.create_from_request(request, post)

    return render(request, 'postv2.html', context)


def post_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "tags.html", context)


def page_about(request):
    return render(request, "about.html")


def page_contact(request):
    return render(request, "contact.html")


def post_search(request):
    if request.method == "GET":
        query = request.GET.get("q")

        if query is not None:
            queryset = Q(title__icontains=query) | Q(body__icontains=query)
            search_results = Post.objects.filter(queryset).distinct()
            context = {"search_results": search_results}
            return render(request, "search_results.html", context)
        else:
            return render(request, "search_results.html")

    else:
        return render(request, "search_results.html")


def yandex(request):
    html = """
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </head>
        <body>Verification: fd81df80c0db7580</body>
    </html>
    """
    return HttpResponse(html)