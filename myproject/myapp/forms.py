from django import forms
from .models import Usuario, ImagenUsuario

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'telefono', 'edad', 'foto_perfil', 'mostrar_whatsapp']

class ImagenUsuarioForm(forms.ModelForm):
    class Meta:
        model = ImagenUsuario
        fields = ['imagen']
