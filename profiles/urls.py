from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/profiles/ <---- path so far
    path('', views.index, name="main-index"),


]