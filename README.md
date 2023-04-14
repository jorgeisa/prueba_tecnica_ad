# Prueba Tecnica Automata Digital Backend
El objetivo del proyecto es implementar un chat entre el usuario y modelos de inteligencia artificial. En este caso se usará GPT3.

## Manual Técnico

### Tabla de Contenidos
* [Herramientas a usar e instalación.](#herramientas-e-instalaciones)
* [Comandos importantes.](#comandos-importantes)
* [Desarrollo de proyecto.](#desarrollo-de-proyecto)

### Herramientas e Instalaciones
En este proyecto se esta usando el sistema operativo Windows.La versión de **Python 3.10.7** con versión **Pip 23.0.1**.

Instalación de **virtualenv** para trabajar con entornos en Python.
```
pip install virtualenv
```

Instalación de **Django** en el entorno virtual. En este caso Django 4.2.
```
pip install django
```

Instalación de herramientas para trabajar con MYSQL **mysqlclient** y **pymysql**. Esto para registrar cada pregunta con su respuesta.
```
pip install mysqlclient pymysql
```

Instalacion de API 

### Comandos importantes

### _virtualenv_
Comando para realizar el entorno virtual.
```
virtualenv env
```

Comando acceder al entrono virtual.
```
.\env\Scripts\activate
```

### _django_
Inicialización del proyecto de Django.
```
django-admin startproject backend .
```

Creación de aplicación en el backend de Django.
```
django-admin startapp api
```

Realizar la migración/tablas de las aplicaciones de Django.
```
python manage.py migrate
```

Creación de superuser en django.
```
python manage.py createsuperuser
```

Crear migración del modelo de las aplicaciones de django.
```
python manage.py makemigrations
```

Ejecutar el servidor de django. Por defecto en el puerto 8000.
```
python manage.py runserver
```



### Desarrollo de Proyecto
Estos comandos son usados dentro del entorno virtual creado (env).

Inicialización del proyecto de Django.
```python
django-admin startproject backend .

# Nos creará una carpeta con los archivos asgi.py, setting.py, urls.py, wsgi.py
```

Creación de aplicación en el backend de Django.
```
django-admin startapp api
```

Se agrega la aplicación de Django a nuestras aplicaciones del proyecto.
```python
# backend>settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
]
```

Cambiamos el idioma si lo deseamos.
```python
# backend>settings.py
LANGUAGE_CODE = 'es-gt'
```

Creamos la base de datos en MySLQ.
![imagen_mysqldb](/img/img01.png)

Tambien editamos la configuración de la base de datos predeterminada y la cambiamos por la de mysql.
```python
# backend>settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'passw0rd',
        'NAME': 'gpt_django',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

Creacion de modelo "Information", como atributos "question" y "answer".
from django.db import models
```python
# Archivo api>models.py
from django.db import models
# Create your models here.
class Information(models.Model):
    question=models.CharField(max_length=3000)
    answer=models.CharField(max_length=3000) 
```

Registro de modelo en el sitio del admin.
```python
# Archivo api>admin.
from django.contrib import admin
from .models import Information
# Register your models here.

admin.site.register(Information)
```

Realizar la migración/tablas de las aplicaciones de Django.
```python
python manage.py migrate
```

Realizar la creación del superuser en django. En este caso le pondremos Usuario: admin y Contraseña. password.
```
$ python manage.py createsuperuser
- Nombre de usuario (leave blank to use 'usuario'): admin
- Dirección de correo electrónico: isaacxicol@gmail.com
- Password: 
- Password (again): 
Esta contraseña es demasiado común.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

Realizar la migración de la aplicación "api" de django. 
```python
python manage.py makemigrations 

# Output:
# Migrations for 'api':
#  api\migrations\0001_initial.py
#    - Create model Information
```

Realizar la migración de nuevo.
```
python manage.py migrate
```


Se puede notar que las tablas en MySQL se han creado correctamente. Esta creado nuestro modelo "api_information".
![Imagen_Mysql_Tables](/img/img02.png)

Ejecutamos el servidor con el siguiente comando.
```
python manage.py runserver
```

Si accedemos al endpoint "localhost:8000/admin/" podremos observar que nuestro servidor se ejcuto correctamente. Ingresamos con las credenciales "admin" y "password" creadas con anterioridad.
![Imagen_Admin_Servidor](/img/img03.png)

Al ingresar observamos la aplicación de django "api" creada con anterioridad. En este caso podemos tambien observar que se ha creado nuestro modelo "Information" correctamente.
![Imagen_Admin_Aplicaciones](/img/img04.png)

Si agregamos dos elementos de "Information" y consultamos nuestra base de datos, veremos que los almacena correctamente.
![Imagen_Agregar_Information](/img/img05.png)

Ahora realizaremos las vistas a partir de una clase que sea capaz de procesar las respuestas.
```python
# Archivo api>views

from django.views import View

# Create your views here.

class InformationView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
```

Ahora agregamos un archivo de urls en la aplicación "api" de django para poder realizar los enpoints correspondientes.
```python
from django.urls import path
from .views import InformationView

urlpatterns = [
    path('informations/', InformationView.as_view(), name='informations_list')
]
```

Registramos las urls recien creadas en la aplicación de Django. Este registro lo hacemos en el archivo "urls.py" del proyecto.
```python
# Archivo backend>urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
```





















