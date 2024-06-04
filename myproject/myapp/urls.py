from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('alert/', views.alert_view, name='alert'),
    path('habitaciones/', views.habitaciones_view, name='habitaciones'),
    path('landing/', views.landing_view, name='landing'),
    path('login/', views.login_view, name='login'),
    path('nuevo/', views.nuevo_view, name='nuevo'),
    path('register/', views.register_view, name='register'),
    path('user/', views.user_view, name='user'),
]
