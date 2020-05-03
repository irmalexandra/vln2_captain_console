from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from consoles.models import Console


def index(request):
    context = {'consoles': Console.objects.all().order_by('name'),
               "consoles_tab": "active"}
    return render(request, 'consoles/index.html', context)


def get_console_by_id(request, id):
    context = {'console': get_object_or_404(Console, pk=id)}
    return render(request, 'consoles/console_details.html', context)
