from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    context = {"users": "active"}
    return render(request, "users/index.html", context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return redirect('profile')
    else:
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def profile_display(request):
    pass
