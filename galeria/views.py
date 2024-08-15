from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Atividade, Curso
from .forms import AtividadeForm, ConteudoForm, UserRegisterForm
from django.shortcuts import render, redirect
from .models import Room, Message, Topico

def index(request):
    cursos = Curso.objects.all()
    cards = {
        1: {'nome': 'Dev Ops', 'legenda': 'BDO/SEM5'},
        2: {'nome': 'Redes', 'legenda': 'RDS/SEM4'}
    }
    return render(request, 'galeria/index.html', {"cursos": cursos, "cards": cards})

def imagem(request):
    return render(request, 'galeria/imagem.html')

def novaAtividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AtividadeForm()
    return render(request, 'galeria/novaAtividade.html', {'form': form})

def novoConteudo(request):
    if request.method == 'POST':
        form = ConteudoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ConteudoForm()
    return render(request, 'galeria/novoConteudo.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'galeria/registro.html', {'form': form})

def CreateRoom(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
        return redirect('room', room_name=room, username=username)
    return render(request, 'galeria/index.html')

def MessageView(request, room_name, username):
    room = Room.objects.get(room_name=room_name)
    messages = Message.objects.filter(room=room)

    if request.method == 'POST':
        message_text = request.POST['message']
        new_message = Message.objects.create(
            room=room,
            sender=username,
            message=message_text
        )
        
        # Criação do tópico associando a mensagem
        Topico.objects.create(
            titulo=message_text[:50],  # Usar os primeiros 50 caracteres como título do tópico
            criador=request.user,
            room=room
        )
        
        return redirect('room', room_name=room_name, username=username)

    return render(request, 'galeria/message.html', {
        'room_name': room_name,
        'username': username,
        'messages': messages
    })

def CreateTopicoView(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        username = request.user.username
        room_name = f"room_{titulo.replace(' ', '_')}"
        
        # Criação da sala associada ao tópico
        new_room = Room.objects.create(room_name=room_name)
        
        # Criação do tópico
        new_topico = Topico.objects.create(titulo=titulo, criador=request.user, room=new_room)
        
        return redirect('room', room_name=new_room.room_name, username=username)
    else:
        topicos = Topico.objects.all()
        return render(request, 'galeria/imagem.html', {'topicos': topicos})

def ImagemView(request):
    topicos = Topico.objects.all()
    if not topicos:
        print("Nenhum tópico encontrado.")
    else:
        print(f"Número de tópicos encontrados: {topicos.count()}")

    return render(request, 'galeria/imagem.html', {'topicos': topicos})
