from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from games.models import Game


def index(request):
    context = {'games': Game.objects.all().order_by('name')}
    return render(request, 'games/index.html', context)


def test(request):
    return render(request, 'games/test.html')

def get_game_by_id(request, id):
    context = { 'game' : get_object_or_404(Game, pk=id)}
    return render(request, 'games/game_details.html', context)
