from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = RichTextField(null=False, blank=False)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Conteudo(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    arquivo = models.FileField(upload_to='conteudos/')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return f'Conteúdo [titulo={self.titulo}]'

class Grupo(models.Model):
    group_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = RichTextField(null=False, blank=False)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    activity_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = RichTextField(null=False, blank=False)
    data_entrega = models.DateField(null=False, blank=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Atividade [titulo={self.titulo}]'

class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name

class Topico(models.Model):
    titulo = models.CharField(max_length=255)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.sender}: {self.message}"