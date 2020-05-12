from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from consoles.models import Console
from games.models import Game, Genre
from main.views import add_recently_viewed
from users.models import Profile, Review, GameReview

# Create your views here.
SORT_DICT = {
    1: 'name',
    2: '-name',
    3: 'price',
    4: '-price',
    5: 'copies_sold',
    6: '-copies_sold',
    7: '-release_date',
    8: 'release_date',
    9: '-rating',
    10: 'rating'
}
SORT_LABELS = {
    1: 'A-Z',
    2: 'Z-A',
    3: 'Price: Low to High',
    4: 'Price: High to Low',
    5: 'Least Popular',
    6: 'Top Sellers',
    7: 'Latest',
    8: 'Oldest',
    9: 'Rating: Highest-Lowest',
    10: 'Rating: Lowest-Highest'
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
               'consoles': Console.objects.all().order_by('name'),
               'sort_dict': SORT_LABELS}

    if genre_id:
        if type(genre_id).__name__ == 'int':
            request.session['genre'] = genre_id
        else:
            request.session.pop('genre', None)

    if console_id:
        if type(console_id).__name__ == 'int':
            request.session['console'] = console_id
        else:
            request.session.pop('console', None)

    if sort:
        if type(sort).__name__ == 'int':
            request.session['sort'] = sort

    if 'genre' not in request.session:
        context['genre_label'] = 'All'
    if 'console' not in request.session:
        context['console_label'] = 'All'
    if 'sort' not in request.session:
        context['sort_label'] = SORT_LABELS[1]

    if 'genre' in request.session and 'console' in request.session and 'sort' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre'],
                                               console_id=request.session['console']).order_by(
            SORT_DICT[request.session['sort']])
        context['genre_label'] = Genre.objects.filter(id=request.session['genre']).first().name
        context['console_label'] = Console.objects.filter(id=request.session['console']).first().name
        context['sort_label'] = SORT_LABELS[request.session['sort']]
        return render(request, 'games/index.html', context)

    elif 'genre' in request.session and 'sort' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre']).order_by(
            SORT_DICT[request.session['sort']])
        context['genre_label'] = Genre.objects.filter(id=request.session['genre']).first().name
        context['sort_label'] = SORT_LABELS[request.session['sort']]
        return render(request, 'games/index.html', context)

    elif 'console' in request.session and 'sort' in request.session:
        context['games'] = Game.objects.filter(console_id=request.session['console']).order_by(
            SORT_DICT[request.session['sort']])
        context['console_label'] = Console.objects.filter(id=request.session['console']).first().name
        context['sort_label'] = SORT_LABELS[request.session['sort']]
        return render(request, 'games/index.html', context)

    elif 'genre' in request.session and 'console' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre'],
                                               console_id=request.session['console']).order_by('name')
        context['genre_label'] = Genre.objects.filter(id=request.session['genre']).first().name
        context['console_label'] = Console.objects.filter(id=request.session['console']).first().name
        return render(request, 'games/index.html', context)

    elif 'genre' in request.session:
        context['games'] = Game.objects.filter(genres=request.session['genre']).order_by('name')
        context['genre_label'] = Genre.objects.filter(id=request.session['genre']).first().name
        return render(request, 'games/index.html', context)

    elif 'console' in request.session:
        context['games'] = Game.objects.filter(console_id=request.session['console']).order_by('name')
        context['console_label'] = Console.objects.filter(id=request.session['console']).first().name
        return render(request, 'games/index.html', context)

    elif 'sort' in request.session:
        context['games'] = Game.objects.all().order_by(SORT_DICT[request.session['sort']])
        context['sort_label'] = SORT_LABELS[request.session['sort']]
        return render(request, 'games/index.html', context)

    else:
        context['games'] = Game.objects.all().order_by('name')
        return render(request, 'games/index.html', context)


def get_game_by_id(request, id):
    context = {}

    add_recently_viewed(request, id)

    reviews = Review.objects.filter(gameID_id=id)
    if reviews:
        context['reviews'] = reviews

    context['product'] = get_object_or_404(Game, pk=id)
    context['product_id'] = id
    return render(request, 'product_details.html', context)


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
        reviews = Review.objects.filter(gameID_id=request.POST['product_id'])
        if reviews:
            recommendations = 0
            for review in reviews:
                if review.recommend:
                    recommendations += 1

            recommendations /= len(reviews)
            recommendations *= 100
        game = Game.objects.filter(id=product_id).first()
        game.rating = recommendations
        game.save()

    return HttpResponse("Check")
