from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50) 
    nacionalidade = models.CharField(null=True, blank=True, max_length=100 )

    def __str__(self):
        return f"{self.nome.upper()} ({self.id})"

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao 
    
    class Meta:
        verbose_name_plural = "Cores"
