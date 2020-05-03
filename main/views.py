from django.shortcuts import render, redirect

# Create your views here.
from games import views


def index(request):
    top_sellers = views.get_game_by_copies_sold(request)
    for thing in top_sellers['top_sellers']:
        print(thing)
    return render(request, 'main/index.html', top_sellers)
