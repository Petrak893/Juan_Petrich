from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    es_dibujante = models.BooleanField(default=False)
    es_escritor = models.BooleanField(default=False)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return self.nombre