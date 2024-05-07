from django.urls import path, include
from game_app.views import list_games, detail_game

urlpatterns = [
    path('', list_games, name="list_games"),
    path('search/', list_games, name="search"),
    path('detail_game/<int:id>/', detail_game, name="detail_game"),
    path('games-by-tag/<int:tag_id>', list_games, name="games_by_tag"),
    path('games-by-category/<int:cat_id>', list_games, name="games_by_category")
]