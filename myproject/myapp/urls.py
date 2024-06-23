from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('home/', views.home_view, name='home'),
    path('alert/', views.alert_view, name='alert'),
    path('habitaciones/', views.HabitacionesView.as_view(), name='habitaciones'),
    path('nuevo/', views.nuevo_view, name='nuevo'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('user/', views.user_view, name='user'),
    path('logout/', views.logout_view, name='logout'),
    path('alojamiento/<int:alojamiento_id>/', views.alojamiento_detalle_view, name='alojamiento_detalle'),
]
