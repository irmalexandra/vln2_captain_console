from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"offers": "active"}
    return render(request, "offers/index.html", context)
