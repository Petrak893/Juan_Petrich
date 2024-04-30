from django.db import models

class cliente(models.Model):
    nombre = models.CharField(max_length=200)