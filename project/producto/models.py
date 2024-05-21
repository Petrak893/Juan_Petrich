from django.db import models
from django.utils import timezone

class ProductoCategoria(models.Model):
    """"Categoria de productos"""
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    num_serie = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "categoria de producto"
        verbose_name_plural = "categoria de productos"

class Producto(models.Model):
    categoria_id = models.ForeignKey(ProductoCategoria, null=True, blank=True, on_delete=models.SET_NULL),
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=100)
    cantidad = models.FloatField()
    precio = models.FloatField()
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateField(null=True, blank=True, default=timezone.now, editable=False, verbose_name="Fecha de actualizacion")

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_medida}) ${self.precio:.2f}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos" 