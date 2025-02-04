# Proyecto Base para desarrollo del backend con docker

Este es una base o estructura basica para implementar en los proyectos version de python 3.7, usando todo con docker

`Para correr el proyecto primero se comenta ciudad en person luego migraciones, si las migraciones se eliminaron`

### Pre-requisitos
1. Install docker y docker compose

### inicio 

1. iniciar pre-configuraciones
    * abre una terminal y digita
      `make start-configure`
2. Crear un usuario super admin
    * abre una terminal y digita
      `make superuser`
3. El sistema ya esta listo para inciar el flujo normal

# Crear Documentacion
1. Crear una carpeta en la raiz del proyecto que se llame doc
2. entrar en esa carpeta y dar el siguiente comando `sphinx-quickstart`
3. Se creara unos archivos, luego buscamos en esa carpeta en el archivo `conf.py` pegamos la estructura que tenemos 
4. luego ejecutamos el siguiente comando `sphinx-apidoc -o modules ..`
5. Recordar que todo se llama y se organiza en index.rst
6. luego hacer `make html`.
7. Guia --> https://davidcasr.medium.com/c%C3%B3mo-documentar-un-proyecto-django-con-sphinx-80e4a090896e
# Variables de entorno
* Archivo de varibles de entorno .env
```
#Django DB
#Django DB
POSTGRES_DB=admin_evoting
POSTGRES_USER=admin_evoting
POSTGRES_PASSWORD=admin_evoting.
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

#Config django
SECRET_KEY= django-insecure-_33yemiuffdbatcf@w#d!8e7^cj6cn=x^q(*w+mna1reubk_i=
DEBUG=True
DJANGO_SETTINGS_MODULE=backend.settings.dev

#Email
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=pruebas.jcsq@gmail.com
EMAIL_HOST_PASSWORD=xbaqniydkrfdwcph
DEFAULT_FROM_EMAIL=pruebas.jcsq@gmail.com

#Db_test
DB_NAME_TEST=admin_evoting_test
DB_USER_TEST=admin_evoting_test
DB_PASS_TEST=admin_evoting_test.
DB_SERVICE_TEST=postgres
DB_PORT_TEST=5432

#Geoposition
GEOPOSITION_GOOGLE_MAPS_API_KEY=AIzaSyBnmNuFL9tmyYs_eCqIjcK8TBwOnM10oVE

#Redis
REDIS_HOST=redis
REDIS_PORT=6379
```
# configuracion correo
A continuacion explicaremos como se configura el gmail para el envio de correos
1.  dirigite a la siguiente pagina https://myaccount.google.com/?utm_source=sign_in_no_continue&pli=1
2. En el menu de la izquierda nos dirigimos al apartado `Seguridad`
3. En el apartado de `Seguridad` buscamos `Acceso a Google`
4. Si no tenemos activado la `Verificacion en 2 pasos` la `ACTIVAMOS`
5. Una vez `ACTIVADA` la `Verificacion en 2 pasos` damos clic en `Contraseñas de aplicacion`
6.  nos saldra la siguiente interzas ![img.png](img.png)
    * Damos clic en `seleccionar app` escogemos la aplicacion que nos conviene
    * luego damos clic en `Seleccionar dispositivo` escogemos nuestro dispositivo
    * le damos clic en `GENERAR` y de la interfaz `copiamos la contraseña que genera` esta misma la pegamos en las variables de entorno (.env) como `EMAIL_HOST_PASSWORD`

# Makefile
En el se encuentran comandos configurados para la facilidad, 
ejecucion y desarrollo del proyecto; los comandos 
disponibles son:


* Ejecutar migraciones
``` bash
make migrate
```
* correr el servidor
``` bash
make up
```
* Crear superusuario
``` bash
make superuser
```
* Crear app
``` bash
make app name=my_app
```
* correr los test
``` bash
make test
```
* Entrar a la terminal de python
``` bash
make shell
```
* Instalar requerimientos
``` bash
make requirements
```
* Exportar los datos a json
``` bash
make export_data
```
* Cargar datos al sistema del archivo disponible
``` bash
make import_data
```
* Vaciar Base de datos
``` bash
make clean_data
```

* Cargar los estaticos
``` bash
make statics
```
  
### Readme development
* Desarrollando la app en local

  1.`make migrate` prepara y carga las migraciones.
       
  2.`make up` corre el servidor local para desarrollo.
* Configuracion run o debuguer

    Para configurar el run o el debuguer se deja toda la estructura 
    tal y como esta, pero adicional se le agrega los siguientes datos:
  1. `HOSTS` tendra como valor `0.0.0.0`
  2. `Environment variables` tendra como valor `PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=backend.settings.dev;TZ=America/Bogota`
  3. `Command and options` tendra como valor `up --exit-code-from django --abort-on-container-exit django nginx celery`
    
