from django.shortcuts import render


def resume_index(request):
    return render(request, "resume_index.html")
