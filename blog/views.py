from django.shortcuts import render
from blog.models import Post

# TODO: Comments
# from .forms import CommentForm


def posts(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "posts.html", context)


def categories(request, category):
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


def post(request, pk):
    post = Post.objects.get(pk=pk)

    # TODO: Comments
    # form = CommentForm()
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = Comment(
    #             author=form.cleaned_data["author"],
    #             body=form.cleaned_data["body"],
    #             post=post
    #         )
    #         comment.save()

    context = {
        "post": post,
        # "comments": comments,  # TODO: Comments
        # "form": form, # TODO: Comments
    }

    return render(request, "post.html", context)
