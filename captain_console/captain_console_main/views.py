from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'test.html')

def games(request):
    return render(request, 'captain_console_main/../templates/captain_console_games/games.html')