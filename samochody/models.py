from django.db import models


class Marka(models.Model):
    nazwa_marki = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa_marki


class Model(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    nazwa_modelu = models.CharField(max_length=50)
    liczba_cylindrow = models.IntegerField(default=4)

    def __str__(self):
        return self.nazwa_modelu
