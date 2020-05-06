from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.update_profile_form import EditProfileForm, EditUserForm
from users.forms.register_form import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

INFO_KEY_DICT = {'username': '', 'email': '', 'first_name': '', 'last_name': '', 'address_1': '',
                 'address_2': '', 'city': '', 'postcode': '', 'country': '', 'profile_image': ''}
LABEL_DICT = {'username': 'Username', 'email': 'Email', 'first_name': 'First name', 'last_name': 'Last name',
              'address_1': 'Address 1',
              'address_2': 'Address 2', 'city': 'City', 'postcode': 'Postcode', 'country': 'Country',
              'profile_image': 'Profile image'}

def index(request):
    context = {"users": "active"}
    return render(request, "users/index.html", context)


def user_login(request):
    username = request.GET.get('username')
    password = request.GET.get('pwd')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('loggedin')
    else:
        return HttpResponse('badcredentials')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username') # for a registration successful message
            return redirect('/users/login')
        else:
            return render(request, 'users/register.html', {
                'form': form
            })
    return render(request, 'users/register.html', {
        'form': RegisterForm()
    })


@login_required
def profile(request):

    user = User.objects.filter(username=request.user.username).first()
    current_profile = Profile.objects.filter(user=request.user).first()
    if current_profile == None:
        current_profile = Profile(user_id=user.id)
        current_profile.save()
    profile_dict = current_profile.__dict__
    user_dict = user.__dict__

    for key in INFO_KEY_DICT:
        if key in profile_dict:
            INFO_KEY_DICT[key] = profile_dict[key]
        elif key in user_dict:
            INFO_KEY_DICT[key] = user_dict[key]

    complete_info_dict = dict((LABEL_DICT[key], value) for (key, value) in INFO_KEY_DICT.items())

    return render(request, 'users/profile.html', {
        'info_dict': complete_info_dict
    })


@login_required
def update_profile(request):
    current_profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        profile_form = EditProfileForm(instance=current_profile, data=request.POST)
        user_form = EditUserForm(instance=current_profile.user, data=request.POST)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')

    return render(request, 'users/update_profile.html', {
        'profile_form': EditProfileForm(instance=current_profile),
        'user_form': EditUserForm(instance=current_profile.user)
    })
