from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from consoles.models import Console
from games.models import Game, Genre
from users.models import Profile, Review, GameReview

# Create your views here.
SORT_DICT = {
    1: 'name',
    2: '-name',
    3: 'price',
    4: '-price',
    5: 'copies_sold',
    6: '-copies_sold',
    7: '-release_date'
}


def genre_filter_view(request, id):
    return filter_sorter(request, id)


def console_filter_view(request, id):
    return filter_sorter(request, None, id)


def game_sort_view(request, id):
    return filter_sorter(request, None, None, id)


def game_default_view(request):
    request.session.pop('genre', None)
    request.session.pop('console', None)
    request.session.pop('sort', None)
    return filter_sorter(request)


def filter_sorter(request, genre_id=None, console_id=None, sort=None):
    context = {"games_tab": "active",
               'genres': Genre.objects.all().order_by('name'),
               'consoles': Console.objects.all().order_by('name')}

    if genre_id:
        request.session['genre'] = genre_id
    if console_id:
        request.session['console'] = console_id
    if sort:
        request.session['sort'] = sort

    if 'genre' in request.session and 'console' in request.session and 'sort' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre'],
                                               console_id=request.session['console']).order_by(
            SORT_DICT[request.session['sort']])
        return render(request, 'games/index.html', context)

    elif 'genre' in request.session and 'sort' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre']).order_by(
            SORT_DICT[request.session['sort']])
        return render(request, 'games/index.html', context)

    elif 'console' in request.session and 'sort' in request.session:
        context['games'] = Game.objects.filter(console_id=request.session['console']).order_by(
            SORT_DICT[request.session['sort']])

    elif 'genre' in request.session and 'console' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre'],
                                               console_id=request.session['console']).order_by('name')
        return render(request, 'games/index.html', context)

    elif 'genre' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre']).order_by('name')
        return render(request, 'games/index.html', context)

    elif 'console' in request.session:
        context['games'] = Game.objects.filter(console_id=request.session['console']).order_by('name')
        return render(request, 'games/index.html', context)

    elif 'sort' in request.session:
        context['games'] = Game.objects.all().order_by(SORT_DICT[request.session['sort']])
        return render(request, 'games/index.html', context)

    else:
        context['games'] = Game.objects.all().order_by('name')
        return render(request, 'games/index.html', context)


# def index_ascending(request):
#     context = {'games': Game.objects.all().order_by('name'),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)
#
#
# def index_descending(request):
#     context = {'games': Game.objects.all().order_by('-name'),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)
#
#
# def sort_by_price_ascending(request):
#     context = {'games': Game.objects.all().order_by('price'),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)
#
#
# def sort_by_price_descending(request):
#     context = {'games': Game.objects.all().order_by('-price'),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)
#
#
# def sort_by_most_popular(request):
#     context = {'games': Game.objects.all().order_by('copies_sold'),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)
#
#
# def sort_by_most_popular(request):
#     context = {'games': Game.objects.all().order_by('-copies_sold'),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)


def get_game_by_id(request, id):
    reviews = Review.objects.filter(gameID_id=id)
    context = {}
    if reviews:
        context['reviews'] = reviews
        recommendations = 0
        for review in reviews:
            if review.recommend:
                user = review.profileID.user.username
                print(review.recommend)
                recommendations += 1
                print(recommendations)

        recommendations /= len(reviews)
        print(recommendations)
        recommendations *= 100
        print(recommendations)
        context['recommendations'] = recommendations
    context['game'] = get_object_or_404(Game, pk=id)
    context['product_id'] = id
    return render(request, 'games/game_details.html', context)


def get_game_by_copies_sold():
    games = Game.objects.all().order_by('-copies_sold')
    return games


def get_game_latest_releases():
    games = Game.objects.all().order_by('-release_date')
    return games


def get_game_offers(request):
    return Game.objects.filter(onSale=True)


@login_required
def add_review(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == "POST":
        feedback = request.POST['feedback']
        recommend = request.POST['recommend']
        date = datetime.date.today()
        profile_id = profile.id
        product_id = request.POST['product_id']
        review = Review.objects.filter(profileID_id=profile_id, gameID_id=product_id)
        if review:
            review.update(feedback=feedback, recommend=recommend)
        else:
            Review.objects.create(recommend=recommend,
                                  feedback=feedback,
                                  datetime=date,
                                  profileID_id=profile_id,
                                  gameID_id=product_id)

    return HttpResponse("Check")


# def filter_by_genre(request, id):
#     context = {'games': Game.objects.filter(genres=id),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)
#
#
# def filter_by_console(request, id):
#     context = {'games': Game.objects.filter(console_id=id),
#                "games_tab": "active",
#                'genres': Genre.objects.all().order_by('name'),
#                'consoles': Console.objects.all().order_by('name')}
#     return render(request, 'games/index.html', context)
#     return render(request, 'games/index.html', context)
