import datetime
from itertools import chain
from django.shortcuts import render
from consoles.models import Console
from games.models import Game
from users.models import Profile, SearchHistory, RecentlyViewedGames, RecentlyViewedConsoles


def index(request):
    """
    Returns a dictionary of set queries
    @param request:
    @return context:
    """
    top_sellers = get_game_by_copies_sold()
    releases = get_game_latest_releases()

    context = {'top_sellers': top_sellers, 'release_date': releases}
    recently_viewed = get_recently_viewed(request)
    context['recently_viewed'] = recently_viewed

    return render(request, 'main/index.html', context)


def search(request):
    """
    Pushes new search instances to the database tied to a profileID
    @param request:
    @return context:
    """
    search_string = request.GET.get('search_field')
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        search_instance = SearchHistory.objects.create(profileID=profile, search=search_string)
        search_instance.save()

    games = Game.objects.filter(name__icontains=search_string)
    consoles = Console.objects.filter(name__icontains=search_string)
    return render(request, 'main/search_results.html', {'games': games,
                                                        'consoles': consoles})


def get_recently_viewed(request):
    products = []
    if request.user.is_authenticated:
        recent_games = RecentlyViewedGames.objects.filter(profileID_id=request.user.profile.id).order_by('-date')
        recent_consoles = RecentlyViewedConsoles.objects.filter(profileID_id=request.user.profile.id).order_by('-date')
        recent_products = sorted(chain(recent_games, recent_consoles), key=lambda prod: prod.date, reverse=True)
        for product in recent_products:
            if type(product).__name__ == 'RecentlyViewedGames':
                products.append(product.gameID)
            else:
                products.append(product.consoleID)
    else:
        if 'recent_viewed' in request.session:
            for id in request.session['recent_viewed']:
                product = Game.objects.filter(id=id).first()
                if product:
                    products.append(product)
                else:
                    product = Console.objects.filter(id=id).first()
                    if product:
                        products.append(product)

    return products


def add_recently_viewed(request, id, game=True):
    if request.user.is_authenticated:
        if game:
            recent = RecentlyViewedGames.objects.filter(gameID=id, profileID_id=request.user.profile.id).first()
            if recent is None:
                RecentlyViewedGames.objects.create(gameID=Game.objects.filter(id=id).first(),
                                                   profileID_id=request.user.profile.id)
            else:
                recent.date = datetime.datetime.now()
                recent.save()
        else:
            recent = RecentlyViewedConsoles.objects.filter(consoleID=id,
                                                           profileID_id=request.user.profile.id).first()
            if recent is None:
                RecentlyViewedConsoles.objects.create(consoleID=Console.objects.filter(id=id).first(),
                                                      profileID_id=request.user.profile.id)
            else:
                recent.date = datetime.datetime.now()
                recent.save()
    else:
        if 'recent_viewed' not in request.session:
            request.session['recent_viewed'] = []
        if id in request.session['recent_viewed']:
            index1 = request.session['recent_viewed'].index(id)
            request.session['recent_viewed'].insert(0, request.session['recent_viewed'][index1])
            request.session['recent_viewed'].pop(index1 + 1)
        else:
            if len(request.session['recent_viewed']) >= 4:
                request.session['recent_viewed'].pop()
            request.session['recent_viewed'].insert(0, id)
        request.session.save()




def get_game_by_copies_sold():
    games = Game.objects.all().order_by('-copies_sold')
    return games


def get_game_latest_releases():
    games = Game.objects.all().order_by('-release_date')
    return games
