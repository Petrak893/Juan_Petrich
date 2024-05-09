from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Nombre(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='nombre_rel')
    nombre = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Telefono(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='telefono_rel')
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.telefono

class Email(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True, blank=True,  related_name='email_rel')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.email
    