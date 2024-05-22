from django.db import models
from django.utils import timezone

""""Nivel del Mutante"""
class NivelMutante(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    num_nivel = models.IntegerField(null=True, blank=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Nivel del Mutante"
        verbose_name_plural = "Nivel de los Mutantes"

class Personaje(models.Model):
    categoria_id = models.ForeignKey(NivelMutante, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=100)
    nombre_real = models.CharField(max_length=100)
    poderes = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    biografia = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    fecha_creacion = models.DateField(default=timezone.now, null=True, blank=True, editable=False, verbose_name="Fecha de creacion")

    def __str__(self) -> str:
        categoria_nombre = self.categoria_id.nombre if self.categoria_id else "Sin categoría"
        return f"{self.nombre} ({self.nombre_real}), Categoría: {categoria_nombre}"

    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes" 