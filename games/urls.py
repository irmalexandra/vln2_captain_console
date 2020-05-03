from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/games/  <--- Path so far
    path('', views.index, name="games-index"),
    path('<int:id>', views.get_game_by_id, name="game_details"),
    path('test', views.get_game_by_copies_sold)
]