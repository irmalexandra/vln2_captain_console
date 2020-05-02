from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"consoles_tab": "active"}
    return render(request, "consoles/index.html", context)