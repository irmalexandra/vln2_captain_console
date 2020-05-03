from django.shortcuts import render, redirect

# Create your views here.
from games import views


def index(request):
    top_sellers = views.get_game_by_copies_sold()
    releases = views.get_game_latest_releases()
    context = {'top_sellers': top_sellers, 'release_date': releases}
    return render(request, 'main/index.html', context)


