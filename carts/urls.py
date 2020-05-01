from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/carts/   <---- Path so far
    path('', views.index, name="carts-index"),
]