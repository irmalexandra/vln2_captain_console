from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"carts": "active"}
    return render(request, "carts/index.html", context)
