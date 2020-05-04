from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # localhost:8000/users/ <---- path so far
    path('', RedirectView.as_view(url='login'), name="login"),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name="users/login.html", redirect_authenticated_user="True"), name="login"),
    path('logout', LogoutView.as_view(next_page="/"), name="logout"),
    path('profile', views.profile, name="profile"),
    path('profile/edit', views.update_profile, name="update_profile")
]