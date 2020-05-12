import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from consoles.models import Console
from main.views import add_recently_viewed
from users.models import RecentlyViewed

SORT_DICT = {
    1: 'name',
    2: '-name',
    3: 'price',
    4: '-price',
    5: '-release_date',
    6: 'release_date',

}
CONSOLE_SORT_LABELS = {
    1: 'A-Z',
    2: 'Z-A',
    3: 'Price: Low to High',
    4: 'Price: High to Low',
    5: 'Latest',
    6: 'Oldest',
}


def console_sort_view(request, id):
    return sorter(request, id)


def console_default_view(request):
    request.session.pop('console_sort', None)
    return sorter(request)


def sorter(request, sort=None):
    context = {"consoles_tab": "active",
               'console_sort_dict': CONSOLE_SORT_LABELS}

    if sort:
        if type(sort).__name__ == 'int':
            request.session['console_sort'] = sort

    if 'console_sort' not in request.session:
        context['console_sort_label'] = CONSOLE_SORT_LABELS[1]

    if 'console_sort' in request.session:
        context['consoles'] = Console.objects.all().order_by(SORT_DICT[request.session['console_sort']])
        context['console_sort_label'] = CONSOLE_SORT_LABELS[request.session['console_sort']]
        return render(request, 'consoles/index.html', context)

    else:
        context['consoles'] = Console.objects.all().order_by('name')
        return render(request, 'consoles/index.html', context)


def get_console_by_id(request, id):
    add_recently_viewed(request, id)
    context = {'product': get_object_or_404(Console, pk=id)}
    return render(request, 'product_details.html', context)


def get_console_by_copies_sold(request):
    consoles = Console.objects.all().order_by('-copies_sold')
    return consoles


def get_console_latest_releases(request):
    consoles = Console.objects.all().order_by('-release_date')
    return consoles


def get_console_offers(request):
    return Console.objects.filter(onSale=True)
