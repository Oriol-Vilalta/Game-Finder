from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Platform, Genre, Game, DevelopingCompany
from .forms import GameForm




# Create your views here.
def home(request):
    plataform = Platform.objects.all()
    genre = Genre.objects.all()
    dev_company = DevelopingCompany.objects.all()
    game=Game.objects.all()
    return render(request, 'home.html',{'platform':plataform, 'genre':genre, 'developing_company':dev_company, 'game':game})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def platforms(request):
    plataform = Platform.objects.all()
    genre = Genre.objects.all()
    dev_company = DevelopingCompany.objects.all()
    game=Game.objects.all()
    return render(request, 'platforms.html',{'platform':plataform, 'genre':genre, 'developing_company':dev_company, 'game':game})


def addGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            """juego = form.save(commit=False)
            juego.usuario = request.user  # Asignar el usuario actual al nuevo juego"""
            # Verificar si el juego ya existe
            titulo = request.POST['title']
            plataforma = request.POST['platform']
            compania = request.POST['developingCompany']
            genero = request.POST['genre']
            if Game.objects.filter(title=titulo, genre=genero).exists():
                messages.error(request, 'Este juego ya existe en la base de datos.')
            else:
                # Si el juego no existe, crearlo
                game = form.save()
                messages.success(request, 'Juego añadido exitosamente.')
                return redirect('home')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})

def deleteGame(request, id_game):
    juego = get_object_or_404(Game, pk=id_game)
    juego.delete()
    #reordenar els id
    juegos = Game.objects.order_by('id')
    for i, juego in enumerate(juegos, start=1):
        juego.id = i
        juego.save()
    #borrar jocs repetits i modificar el id
    games = Game.objects.all()
    unique_games = []
    for game in games:
        if game.title not in [g.title for g in unique_games]:
            unique_games.append(game)
        else:
            see_id = game.id
            game.delete()
            for g in unique_games:
                if g.id > see_id:
                    g.id -= 1
                    g.save()

    return redirect('home')

def updateGame(request, id_game):
    game = get_object_or_404(Game, pk=id_game)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update_game.html', {'form': form})