from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    es_dibujante = models.BooleanField(default=False)
    es_escritor = models.BooleanField(default=False)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_personajes/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores" 