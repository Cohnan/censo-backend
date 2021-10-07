from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, es_coordinador = False): 
        if not email or not password:
            raise ValueError('Los Usuarios deben tener Email y Contraseña')

        usuario = self.model(
            email = self.normalize_email(email),
        )

        usuario.set_password(password)
        usuario.es_coordinador = es_coordinador

        usuario.save(using = self._db)

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = email,
            password = password,
            es_coordinador = False
        )

        usuario.es_admin = True
        
        usuario.save(using = self._db)

        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key = True)
    email = models.EmailField(verbose_name = "Email", max_length = 100, unique = True)
    password = models.CharField(verbose_name = "Contraseña", max_length = 256)
    nombre = models.CharField(verbose_name = 'Nombre', max_length = 50)
    es_coordinador = models.BooleanField(verbose_name = "Es Coordinador", default = False)
    es_admin = models.BooleanField(verbose_name = "Es Administrador", default = False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def save(self, **kwargs):
        sal = 'some_salt'
        self.password = make_password(self.password, sal)
        super().save(**kwargs)
