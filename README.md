# censo-backend

Backend de la aplicación web de Censo de Pueblos Indígena, realizado como proyecto por Equipo 2 del grupo P8 del programa MisiónTIC 2022, Cohorte 2021, Ciclo 3.

# Software Requerido

Se requiere de Python 3.9 y acceso a un servidor del motor de bases de datos PostgreSQL.

# Cómo Correr el Proyecto

0.  Correr una terminal y ubicar su directorio a la raiz de este repositorio.

1. Instalar los requerimientos del proyecto: en la terminal, escribir
```
pip install -r requirements.txt
```

2. Tener servidor de PostgreSQL corriendo.

3. Crear archivo ``db_credentials.json`` dentro de la carpeta ``utils/`` con la siguiente estructura:
```
{
	"db_ip"      : "ip del servidor",
	"db_port"    : "puerto de comunicacion con postgres", 
        "db_name"    : "nombre base de datos",
	"db_user"    : "nombre usuario de la base de datos",
	"db_pass"    : "contraseña del usuario"
}
```

4. Migrar la base de datos: en la linea de comandos escribir
```
python manage.py makemigrations
python manage.py migrate
```

5. Correr la aplicación:
```
python manage.py runserver
```

# Acceder al Proyecto
Al proyecto se acceda a través del puerto ``8000`` del servidor: [ipServidor:8000](ipServidor:8000). Si se está corriendo en una máquina local, la dirección del proyecto será [127.0.0.1:8000](127.0.0.1:8000).

A la aplicación de **Censo de Personas Indígenas** se accede a través del slug ``censoIndigena/``, y a los servicios CRUD de la *Tabla de Personas* registradas a través del slug ``personas/``, es decir a esta tabla se accede a través de la URL [ipServidor:8000/censoIndigena/personas/](ipServidor:8000/censoIndigena/personas/).

