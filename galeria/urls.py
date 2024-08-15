from django.urls import path
from galeria.views import index, imagem, novaAtividade
from django.urls import path
from .views import CreateRoom, MessageView, CreateTopicoView, ImagemView

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', ImagemView, name='imagem'),
    path('novaAtividade/', novaAtividade, name='novaAtividade'),
    path('create-topico/', CreateTopicoView, name='create-topico'),
    path('create-room/', CreateRoom, name='create-room'),
    path('<str:room_name>/<str:username>/', MessageView, name='room'),
]
