from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/consoles/   <---- Path so far
    path('', views.index, name="main-index"),


]