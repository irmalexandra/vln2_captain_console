from django.shortcuts import render, redirect

# Create your views here.
from games import views


def index(request):
    top_sellers = views.get_game_by_copies_sold(request)
    gta = views.get_gta(request)
    return render(request, 'main/index.html', top_sellers)
