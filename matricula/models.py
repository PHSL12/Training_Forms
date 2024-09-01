from django.db import models

# Create your models here.
class Aluno(models.Model):
     nome = models.CharField(max_length=100)
     endereco = models.CharField(max_length=200)
     cidade = models.CharField(max_length=50)
     email = models.EmailField()
     curso = models.CharField(max_length=50)
     
     def __str__(self):
         return self.nome