# censo-backend

Backend de la aplicación web de Censo de Pueblos Indígena, realizado como proyecto por Equipo 2 del grupo P8 del programa MisiónTIC 2022, Cohorte 2021, Ciclo 3.

# Cómo Correr el Proyecto

1. Tener servidor de postgres corriendo

2. Crear archivo ``db_credentials.json`` dentro de la carpeta ``utils`` con la siguiente estructura:
```
{
	"db_ip"      : "ip del servidor",
	"db_port"    : "puerto de comunicacion con postgres", 
    "db_name"    : "nombre base de datos",
	"db_user"    : "nombre usuario de la base de datos",
	"db_pass"    : "contraseña del usuario"
}
```

3. Migrar la base de datos: Estando en la raiz del repositorio, en la linea de comandos escribir lo siguiente
```
python manage.py makemigrations
python manage.py migrate
```

4. Correr el servidor:
```
python manage.py runserver
```
Esto hará que al proyecto se acceda a través del puerto ``8000`` del servidor: [ipServidor:8000](ipServidor:8000). Si se está corriendo en una máquina local, la dirección del proyecto será [127.0.0.1:8000](127.0.0.1:8000]).

A la aplicación de **Censo de Perdonas Indígenas** se accede a través del slug ``censoIndigena/``, y a los servicios CRUD de la tabla de Personas registradas a través del slug ``personas/``, es decir a esta tabla se accede a través de la URL [ipServidor:8000/censoIndigena/personas](ipServidor:8000/censoIndigena/personas/).

