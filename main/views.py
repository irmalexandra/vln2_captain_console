from django.shortcuts import render, redirect

# Create your views here.
from games import views


def index(request):
    top_sellers = views.get_game_by_copies_sold(request)
    gta = views.get_gta(request)
    releases = views.get_game_latest_releases(request)
    context = {'gta': gta, 'top_sellers': top_sellers, 'release_date': releases}
    return render(request, 'main/index.html', context)
