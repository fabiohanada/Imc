from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    peso = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    altura = models.DecimalField(max_digits=3, decimal_places=2)

    def calcular_imc(self):
        if self.altura and self.altura > 0:
            return round(float(self.peso) / (float(self.altura) ** 2), 2)
        return 0.0

    def __str__(self):
        return f"{self.pessoa.nome} - IMC: {self.calcular_imc()}"