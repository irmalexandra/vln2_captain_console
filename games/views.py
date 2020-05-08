from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime

# Create your views here.
from games.models import Game
from users.models import Profile, Review, GameReview


def index_ascending(request):
    context = {'games': Game.objects.all().order_by('name'),
               "games_tab": "active"}
    return render(request, 'games/index.html', context)


def index_descending(request):
    context = {'games': Game.objects.all().order_by('-name'),
               "games_tab": "active"}
    return render(request, 'games/index.html', context)


def sort_by_price_ascending(request):
    context = {'games': Game.objects.all().order_by('price'),
               "games_tab": "active"}
    return render(request, 'games/index.html', context)


def sort_by_price_descending(request):
    context = {'games': Game.objects.all().order_by('-price'),
               "games_tab": "active"}
    return render(request, 'games/index.html', context)


def sort_by_most_popular(request):
    context = {'games': Game.objects.all().order_by('-price'),
               "games_tab": "active"}
    return render(request, 'games/index.html', context)


def sort_by_most_popular(request):
    context = {'games': Game.objects.all().order_by('-copies_sold'),
               "games_tab": "active"}
    return render(request, 'games/index.html', context)


def get_game_by_id(request, id):
    reviews = Review.objects.filter(gameID_id=id)
    context = {}
    if reviews:
        context['reviews'] = reviews
    context['game'] = get_object_or_404(Game, pk=id)
    return render(request, 'games/game_details.html', context)


def get_game_by_copies_sold():
    games = Game.objects.all().order_by('-copies_sold')
    return games


def get_game_latest_releases():
    games = Game.objects.all().order_by('-release_date')
    return games


def get_game_offers(request):
    return Game.objects.filter(onSale=True)


def add_review(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == "POST":
        feedback = request.POST['feedback']
        rating = request.POST['rating']
        date = datetime.date.today()
        profile_id = profile.id
        product_id = request.POST['product_id']
        new_review = Review.objects.filter(profileID_id=profile_id, gameID_id=product_id)
        if new_review:
            new_review.update(feedback=feedback, rating=rating)
        else:
            Review.objects.create(rating=rating,
                                  feedback=feedback,
                                  datetime=date,
                                  profileID_id=profile_id,
                                  gameID_id=product_id)

    return HttpResponse("Check")
