from django.shortcuts import render

def alert_view(request):
    return render(request, 'myapp/alert.html')

def habitaciones_view(request):
    return render(request, 'myapp/habitaciones.html')

def home_view(request):
    return render(request, 'myapp/home.html')

def landing_view(request):
    return render(request, 'myapp/landing.html')

def login_view(request):
    return render(request, 'myapp/login.html')

def nuevo_view(request):
    return render(request, 'myapp/nuevo.html')

def pruebas_view(request):
    return render(request, 'myapp/pruebas.html')

def register_view(request):
    return render(request, 'myapp/register.html')

def user_view(request):
    return render(request, 'myapp/user.html')
