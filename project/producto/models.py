from django.db import models

class ProductoCategoria(models.Model):
    """"Categoria de productos"""
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "categoria de productos"
        verbose_name_plural = "categoria de productos"