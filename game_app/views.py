from django.shortcuts import render, get_object_or_404
from workspace.filtesr import GameFilter
from game_app.models import Category, Game, Tag
from django.core.paginator import Paginator
from django.db.models import Q

def main(request):
    return render(request, 'index.html')


def list_games(request, tag_id=None, cat_id=None):
    form = GameFilter().form
    games = Game.objects.all().order_by('-date')
    search_query = request.GET.get('search')
    search_query2 = request.GET.get('search2')
    if search_query:
        games = games.filter(
            Q(name__contains=search_query) |
            Q(content__contains=search_query)
        )
    if search_query2:
        games = games.filter(
            Q(name__contains=search_query2) |
            Q(content__contains=search_query2)
    )
    if tag_id:
        games = get_object_or_404(Tag, id=tag_id).games.all()
    elif cat_id:
        games = get_object_or_404(Category, id=cat_id).game.all()
    filter_set = GameFilter(queryset=games, data=request.GET)
    games = filter_set.qs
    form = filter_set.form
    paginator = Paginator(games, 6)
    page  = int(request.GET.get('page',1))
    games = paginator.get_page(page)
    return render(request, 'list_games.html', {"form": form, "games":games, "page":page})


def detail_game(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'detail_game.html', {"game":game,})

# Create your views here.
