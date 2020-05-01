from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/captain_console_main
    path('', views.index, name="main-index"),


]