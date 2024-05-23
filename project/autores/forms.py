from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre',
                  'es_dibujante',
                  'es_escritor',
                  'fecha_nacimiento',
                  'biografia',
                  'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'es_dibujante': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'es_escritor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
