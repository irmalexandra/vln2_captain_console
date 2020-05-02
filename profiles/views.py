from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    context = {"profiles": "active"}
    return render(request, "profiles/index.html", context)
