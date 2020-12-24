from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="posts"),
    path("<int:pk>/", views.post, name="post"),
    path("<category>/", views.categories, name="categories"),
]
