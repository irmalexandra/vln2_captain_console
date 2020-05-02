from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    context = {"games": "active"}
    return render(request, 'games/index.html', context)
