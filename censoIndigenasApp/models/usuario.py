from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password

#Kind of along the same lines as above, but for what it's worth you could also go ahead with MinLengthValidator which django supplies. Worked for me. The code would look something like this:

from django.core.validators import MinLengthValidator

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, nombre, es_admin = False):
        # if not email or not password:
        #     raise ValueError('Los Usuarios deben tener Email y Contraseña')

        # Si en la peticion de registro se indico que el usuario fuera admin, hacer uso del 
        # metodo creado para eso
        if es_admin:
            return self.create_superuser(email = email, password = password, nombre = nombre)

        # Usando super clase, poniendo ojala todos los atributos heredados necesarios
        usuario = self.model(
            email = self.normalize_email(email), # Para dominio en minusculas
        )

        # Agregando los atributos adicionales al usuario
        sal = 'condimento'
        usuario.password = make_password(password, sal)
        #usuario.set_password(password)
        usuario.nombre = nombre

        # Guardar en base de datos
        usuario.save(using = self._db) 

        return usuario

    def create_superuser(self, email, password, nombre):
        # Crear un usuario comun y corriente
        usuario = self.create_user(
            email = email,
            password = password,
            nombre = nombre
        )

        # Cambiar a True la propiedad de que es admin
        usuario.es_admin = True
        
        # Guardar en base de datos
        usuario.save(using = self._db) 

        return usuario

class Usuario(AbstractBaseUser):
    id = models.BigAutoField(primary_key = True)
    email = models.EmailField(verbose_name = "Email", max_length = 100, unique = True, blank = False, validators=[MinLengthValidator(4)])
    password = models.CharField(verbose_name = "Contraseña", max_length = 256)
    nombre = models.CharField(verbose_name = 'Nombre', max_length = 50, blank = False, validators=[MinLengthValidator(4)])
    # Propiedad para saber si el usuario tiene derecho de crear nuevos usuarios
    es_admin = models.BooleanField(verbose_name = "Es Administrador", default = False)

    objects = UsuarioManager()

    # Atributo que indica el campo que se usará para identifiación del usuario
    USERNAME_FIELD = 'email'
    
    # Estos son los atributos los pedirá django al momento de decirle createsuperuser
    REQUIRED_FIELDS = ['nombre']

    # Solo se debe hacer una encriptacion de la contrasena, y la estamos haciendo en el UserManager
    # def save(self, **kwargs):
    #     sal = 'condimento'
    #     self.password = make_password(self.password, sal)
    #     super().save(**kwargs)
