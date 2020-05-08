from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/games/  <--- Path so far
    path('', views.index_ascending, name="game_index_ascending"),
    path('name=A_Z', views.index_ascending, name="game_index_ascending"),
    path('name=Z_A', views.index_descending, name="game_index_descending"),
    path('<int:id>', views.get_game_by_id, name="game_details"),
    path('test', views.get_game_by_copies_sold),
    path('price=low_to_high', views.sort_by_price_ascending, name="game_price_ascending"),
    path('price=high_to_low', views.sort_by_price_descending, name="game_price_descending"),
    path('popular', views.sort_by_most_popular, name="game_most_popular"),
    path('add_review', views.add_review, name="add_review")
]