from django.urls import resolve, reverse
from django.shortcuts import redirect, render, get_object_or_404
from workspace.filtesr import GameFilter
from workspace.forms import ChangePasswordForm, GamesForm, LoginForm, RegisterForm, ChangeProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from workspace.decarators import login_required
from game_app.models import *

def register_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('main'))

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать {user} в рабочую зону')
            return redirect(reverse('workspace'))
    return render(request, 'auth_user/register.html', {'form': form})

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username = username, password = password)
            if user:
                login(request,user)
                messages.success(request, f'Это {user} успешно авторизовался')
                return redirect('/workspace')
    return render(request, 'auth_user/login.html', {"form": form})

@login_required(login_url='/workspace/login')
def create_game(request):
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.author = request.user
            game.save()
            messages.success(request, f'Ваша игра "{game.name}" успешна удалена.')
            return redirect('/workspace')
    return render(request, 'workspace/create.html', {"form":form,})

@login_required(login_url='/workspace/login')
def update_game(request, id):
    game = Game.objects.get(id=id)
    form = GamesForm(instance=game)
    if request.method == "POST":
        form = GamesForm(instance=game, data=request.POST, files=request.FILES)
        if form.is_valid():
            game = form.save()
            messages.success(request, f'Ваша игра "{game.name}" успешна обновалена.')
            return redirect('/workspace')
    return render(request, 'workspace/update.html', {"game": game, "form":form})

@login_required(login_url='/workspace/login')
def workspace(request):
    form = GameFilter().form
    games = Game.objects.filter(author=request.user).order_by('-date')
    search_query = request.GET.get('search')
    if search_query:
        games = games.filter(
            Q(name__contains=search_query) |
            Q(content__contains=search_query)
        )
    filter_set = GameFilter(queryset=games, data=request.GET)
    games = filter_set.qs
    form = filter_set.form
    paginator = Paginator(games, 6)
    page  = int(request.GET.get('page',1))
    games = paginator.get_page(page)
    return render(request, 'workspace/index.html', {"form": form, "games":games})

@login_required(login_url='/workspace/login')
def workspace_detail_game(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'workspace/detail_game.html', {"game":game,})

@login_required(login_url='/workspace/login')
def delete_game(request, id):
    game = get_object_or_404(Game, id=id)
    if game:
        game.delete()
    messages.success(request, f'Ваша игра "{game.name}" успешна удалена.')
    return redirect('/workspace')

@login_required(login_url='/workspace/login')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/games')


@login_required(login_url='/workspace/login')
def profile(request):
    return render(request, 'auth_user/profile.html')

@login_required(login_url='/workspace/login')
def change_profile(request):
    user = request.user
    form = ChangeProfileForm(instance=user)
    if request.method == 'POST':
        form = ChangeProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль успешно изменен!')
            return redirect('/workspace/profile')
    return render(request, 'auth_user/change_profile_form.html',{"form": form})


@login_required(login_url='/workspace/login/')
def change_password(request):
    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            confirm_password = form.cleaned_data['confirm_password']
            user = request.user
            user.set_password(confirm_password)
            user.save()
            login(request, user)
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('/workspace/profile')
    return render(request, 'auth_user/change_password.html', {'form': form})

# Create your views here.
