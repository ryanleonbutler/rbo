from django.contrib import admin
from django.urls import include, path

from markdownx import urls as markdownx


urlpatterns = [
    path("admin/", admin.site.urls),
    path("resume/", include("resume.urls")),
    path("", include("blog.urls")),
]

urlpatterns += [path("markdownx/", include(markdownx))]
