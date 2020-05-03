from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from games.models import Game


def index(request):
    context = {'games': Game.objects.all().order_by('name'),
               "games_tab": "active"}
    return render(request, 'games/index.html', context)


def get_game_by_id(request, id):
    context = {'game': get_object_or_404(Game, pk=id)}
    return render(request, 'games/game_details.html', context)


def get_game_by_copies_sold(request):
    games = {'top_sellers': Game.objects.all().order_by('-copies_sold')}
    return games
