from django.db import models

class Nombre(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Telefono(models.Model):
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.telefono

class Email(models.Model):
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.email

class Cliente(models.Model):
    nombre = models.ForeignKey(Nombre, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.ForeignKey(Telefono, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.ForeignKey(Email, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre.nombre if self.nombre else ""

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"