from django.shortcuts import render, redirect

# Create your views here.
from consoles.models import Console
from games import views
from games.models import Game
from main.models import Product
from users.models import Profile, SearchHistory


def index(request):
    """

    :param request:
    :return:
    """
    top_sellers = views.get_game_by_copies_sold()
    releases = views.get_game_latest_releases()

    context = {'top_sellers': top_sellers, 'release_date': releases}

    if request.user.is_authenticated:
        recently_viewed = views.get_recently_viewed(request)
        context['recently_viewed'] = recently_viewed
    return render(request, 'main/index.html', context)


def search(request):
    search_string = request.GET.get('search_field')
    # if request.user.is_authenticated:
    #     profile = Profile.objects.filter(user=request.user).first()
    #     search_instance = SearchHistory.objects.create(profileID=profile, search=search_string)
    #     search_instance.save()

    games = Game.objects.filter(name__icontains=search_string)
    consoles = Console.objects.filter(name__icontains=search_string)
    return render(request, 'main/search_results.html', {'games': games,
                                                        'consoles': consoles})
