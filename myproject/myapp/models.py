from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

class MyUserManager(BaseUserManager):
    def create_user(self, email, nombre, telefono, edad, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, telefono=telefono, edad=edad, username=email)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nombre, telefono, edad, password=None):
        user = self.create_user(email, password=password, nombre=nombre, telefono=telefono, edad=edad)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractUser):
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    edad = models.IntegerField()
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    mostrar_whatsapp = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'telefono', 'edad']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return self.email


class Alojamiento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    latitud = models.FloatField()
    longitud = models.FloatField()
    caracteristicas = models.JSONField()

    def __str__(self):
        return self.nombre

class ImagenAlojamiento(models.Model):
    alojamiento = models.ForeignKey(Alojamiento, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='alojamientos/')

    def __str__(self):
        return f"Imagen de {self.alojamiento.nombre}"
