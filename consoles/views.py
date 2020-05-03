from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from consoles.models import Console


def index(request):
    context = {'consoles': Console.objects.all().order_by('name'),
               "consoles_tab": "active"}
    return render(request, 'consoles/index.html', context)


def get_console_by_id(request, id):
    context = {'console': get_object_or_404(Console, pk=id)}
    return render(request, 'consoles/console_details.html', context)



def get_console_offers(request):
    all = Console.objects.all()
    offers = []
    for console in all:
        if console.onSale == True:
            offers.append(console)
    return offers

def get_console_by_copies_sold(request):
    consoles = Console.objects.all().order_by('-copies_sold')
    return consoles


def get_console_latest_releases(request):
    consoles = Console.objects.all().order_by('-release_date')
    return consoles

