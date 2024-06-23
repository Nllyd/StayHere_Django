from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .models import Usuario, Alojamiento, ImagenAlojamiento
from django.db import IntegrityError


def logout_view(request):
    logout(request)
    return redirect('home')

def landing_view(request):
    return render(request, 'myapp/landing.html')

def alert_view(request):
    return render(request, 'myapp/alert.html')

def home_view(request):
    alojamientos = Alojamiento.objects.all()
    return render(request, 'myapp/home.html', {'alojamientos': alojamientos})

@login_required
def alojamiento_detalle_view(request, alojamiento_id):
    alojamiento = get_object_or_404(Alojamiento, id=alojamiento_id)
    return render(request, 'myapp/habitaciones.html', {'alojamiento': alojamiento})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logueo exitoso')
            return redirect('home')
        else:
            return render(request, 'myapp/login.html', {'error': 'Correo o contraseña incorrectos'})
    return render(request, 'myapp/login.html')

import logging

logger = logging.getLogger(__name__)

@login_required
def nuevo_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        latitud = request.POST['latitud']
        longitud = request.POST['longitud']
        caracteristicas = request.POST.getlist('caracteristicas')
        imagenes = request.FILES.getlist('imagenes')

        logger.info(f"Datos recibidos: {nombre}, {descripcion}, {precio}, {latitud}, {longitud}, {caracteristicas}")

        # Validar que latitud y longitud no estén vacíos
        if not latitud or not longitud:
            messages.error(request, 'Por favor, selecciona una ubicación en el mapa.')
            return render(request, 'myapp/nuevo.html')

        alojamiento = Alojamiento(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            latitud=float(latitud),
            longitud=float(longitud),
            caracteristicas=caracteristicas,
            usuario=request.user
        )
        alojamiento.save()
        
        for imagen in imagenes:
            ImagenAlojamiento.objects.create(alojamiento=alojamiento, imagen=imagen)

        messages.success(request, 'Alojamiento guardado exitosamente.')
        return redirect('home')
    
    return render(request, 'myapp/nuevo.html')

@login_required
def pruebas_view(request):
    return render(request, 'myapp/pruebas.html')

def register_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        edad = request.POST['edad']
        password = request.POST['password']
        
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'myapp/register.html', {'error': 'Correo ya utilizado'})
        
        try:
            usuario = Usuario(nombre=nombre, email=email, telefono=telefono, edad=edad, username=email)
            usuario.set_password(password)
            usuario.save()
            return redirect('home')
        except IntegrityError:
            return render(request, 'myapp/register.html', {'error': 'Error al crear el usuario'})
    return render(request, 'myapp/register.html')

@login_required
def user_view(request):
    return render(request, 'myapp/user.html')

class HabitacionesView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        alojamientos = Alojamiento.objects.all()
        return render(request, 'myapp/habitaciones.html', {'alojamientos': alojamientos})
