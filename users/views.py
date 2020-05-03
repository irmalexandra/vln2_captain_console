from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.update_profile_form import UpdateProfileForm
from users.forms.register_form import RegisterForm


def index(request):
    context = {"users": "active"}
    return render(request, "users/index.html", context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login')
    return render(request, 'users/register.html', {
        'form': RegisterForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'users/profile.html', {
        'form': profile
    })


def update_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UpdateProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'users/update_profile.html', {
        'form': UpdateProfileForm(instance=profile)
    })
