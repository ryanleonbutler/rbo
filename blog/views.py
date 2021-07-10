from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Nibble, Post, Category, NibbleCategory
from blog.utils import get_post_content_from_file


class IndexListView(ListView):
    queryset = Post.objects.filter(status=1).order_by("-publish_date")
    template_name = "index.html"

    def get_object(self, queryset=None):
        return super(IndexListView, self).get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['nibbles'] = Nibble.objects.all()
        return context


class BlogListView(ListView):
    queryset = Post.objects.filter(status=1).order_by("-publish_date")
    context_object_name = "post_list"
    template_name = "blog.html"

    def get_object(self, queryset=None):
        return super(BlogListView, self).get_object(queryset)


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
        context['content'] = get_post_content_from_file(obj.post_path)
        return context


class NibbleListView(ListView):
    queryset = Nibble.objects.filter(status=1).order_by("-publish_date")
    context_object_name = "nibbles_list"
    template_name = "nibbles.html"

    def get_object(self, queryset=None):
        return super(NibbleListView, self).get_object(queryset)


class NibbleDetailView(DetailView):
    model = Nibble
    context_object_name = "nibble_detail"
    template_name = "nibble.html"

    def get_object(self, queryset=None):
        return super(NibbleDetailView, self).get_object(queryset)

    def get_context_data(self, **kwargs):
        obj = super(NibbleDetailView, self).get_object()
        context = super().get_context_data(**kwargs)
        context['content'] = get_post_content_from_file(obj.nibble_path)
        return context


class PostCategoryView(ListView):
    model = Category
    template_name = "tags.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class NibbleCategoryView(ListView):
    model = NibbleCategory
    template_name = "nibble_tags.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nibbles'] = Nibble.objects.all()
        return context


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
