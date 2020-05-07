from django.shortcuts import render, redirect

# Create your views here.
from games import views
from main.models import Product


def index(request):
    print("In main index :o")
    top_sellers = views.get_game_by_copies_sold()
    releases = views.get_game_latest_releases()
    context = {'top_sellers': top_sellers, 'release_date': releases}
    return render(request, 'main/index.html', context)


def search(request):
    search_string = request.GET.get('search_field')
    results = Product.objects.filter(name__icontains=search_string)
    return render(request, 'main/search_results.html', {'search_results': results})
