from django import forms
from . import models

class NivelMutanteForm(forms.ModelForm):
    class Meta:
        model = models.NivelMutante
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "numero del nivel": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            
        }

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = models.Personaje
        fields = "__all__"