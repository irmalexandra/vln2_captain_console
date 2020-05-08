from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from users.models import Profile
from carts.models import ShippingInformation, PaymentInformation
from users.forms.update_profile_form import ProfileForm, UserForm
from users.forms.register_form import RegisterForm
from carts.forms.payment_form import PaymentForm
from carts.forms.shipping_form import ShippingForm
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
    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponse('loggedin')
    else:
        return JsonResponse(form.errors)


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
        profile_form = ProfileForm(instance=current_profile, data=request.POST)
        user_form = UserForm(instance=current_profile.user, data=request.POST)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')

    return render(request, 'users/update_profile.html', {
        'profile_form': ProfileForm(instance=current_profile),
        'user_form': UserForm(instance=current_profile.user)
    })


@login_required
def update_payment_info(request):
    current_profile = Profile.objects.filter(user=request.user).first()
    current_payment_info = PaymentInformation.objects.filter(id=current_profile.payment_information_id.id).first()
    payment_form = PaymentForm(instance=current_payment_info)

    if current_payment_info == None:
        current_payment_info = PaymentInformation()
        current_payment_info.save()

    if request.method == 'POST':
        payment_form = PaymentForm(instance=current_payment_info, data=request.POST)

        if payment_form.is_valid():
            payment_form.save()
            return redirect('profile')
    print()
    return render(request, 'users/update_payment_info.html', {
        'payment_form': payment_form
    })

@login_required
def update_shipping_info(request):
    current_profile = Profile.objects.filter(user=request.user).first()
    current_shipping_info = ShippingInformation.objects.filter(id=current_profile.shipping_information_id.id).first()
    if current_shipping_info == None:
        current_shipping_info = ShippingInformation()
        current_shipping_info.save()

    if request.method == 'POST':
        current_shipping_form = ShippingForm(instance=current_shipping_info, data=request.POST)

        if current_shipping_form.is_valid():
            current_shipping_info.save()
            return redirect('profile')

    return render(request, 'users/update_shipping_info.html', {
        'shipping_form': ShippingForm(instance=current_shipping_info)
    })

