from django import forms
from .models import Usuario, Perfil

class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['biografia']
