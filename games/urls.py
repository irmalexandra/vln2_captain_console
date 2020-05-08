from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/games/  <--- Path so far
    path('', views.game_default_view, name="default_view"),
    path('<int:id>', views.get_game_by_id, name="game_details"),
    #path('name=A_Z', views.index_ascending, name="game_index_ascending"),
    #path('name=Z_A', views.index_descending, name="game_index_descending"),
    #path('copies_sold', views.get_game_by_copies_sold),
    #path('price=low_to_high', views.sort_by_price_ascending, name="game_price_ascending"),
    #path('price=high_to_low', views.sort_by_price_descending, name="game_price_descending"),
    #path('popular', views.sort_by_most_popular, name="game_most_popular"),
    path('add_review', views.add_review, name="add_review"),
    #path('genres/<int:id>', views.filter_by_genre, name="filter_by_genre"),
    #path('console/<int:id>', views.filter_by_console, name="filter_by_console"),
    path('sort/<int:id>', views.game_sort_view, name='game_sort_view'),
    path('filter_by_genre/<int:id>', views.genre_filter_view, name='filter_by_genre'),
    path('filter_by_console/<int:id>', views.console_filter_view, name='filter_by_console'),
]