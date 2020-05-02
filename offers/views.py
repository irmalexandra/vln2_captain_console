from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"offers_tab": "active"}
    return render(request, "offers/index.html", context)
