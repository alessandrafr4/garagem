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

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="livros")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="livros")

    ano = models.IntegerField(max_length=32, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)

    
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros")
    Editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")


    def __str__(self):
        return f"{self.nome.upper()} ({self.id})"

        
