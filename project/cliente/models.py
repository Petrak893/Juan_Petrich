from django.db import models

class Nombre(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Telefono(models.Model):
    num_tel = models.IntegerField
    Nombre = models.ForeignKey(Nombre, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.num_tel

class Email(models.Model):
    correo_e = models.EmailField
    nombre = models.ForeignKey(Nombre, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.correo_e
    
class Cliente(models.Model):
    nombre = models.ForeignKey(Nombre, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.ForeignKey(Telefono, on_delete=models.SET_NULL, null=True, blank=True)
    correo_e = models.ForeignKey(Email, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
