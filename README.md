# Prueba Tecnica Automata Digital Backend
El objetivo del proyecto es implementar un chat entre el usuario y modelos de inteligencia artificial. En este caso se usará gpt-3.5-turbo. En este proyecto solamente esta el backend desarrollado en Django.

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

Instalacion de OpenAI en Python
```
pip install openai
```

Instalacion de django-corse-headers
```
python -m pip install django-cors-headers
```

Para poder consumir nuestra API en django es necesario activar el CORS en Django. Por lo que debemos editas las siguientes partes de nuestro codigo en el archivo "settings.py" de nuestro proyecto. En este repositorio estan los pasos: [Repositorio Cors.](https://github.com/adamchainz/django-cors-headers)

```python
#Archivo backend>settings.py
INSTALLED_APPS = [
    ...
    "corsheaders",
    ...
]

MIDDLEWARE = [
    ...
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...
]

...
CORS_ALLOW_ALL_ORIGINS = True
...
```



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

Ahora realizaremos las vistas a partir de una clase que sea capaz de procesar las respuestas (GET, POST).
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

Seguimos editando las views en la aplicación "api" de Django.

El metodo "post" de nuestro view se encargará de obtener una respuesta de la pregunta/consulta/frase (prompt) que el usuario realice desde el frontend. La respuesta sera generada por _**GPT-3.5-turbo**_. Se escogió esto debido que _gpt-4_ esta en fase beta no accesible para todos.

Realizamos un archivo llamado "secret_key.py" que será la llave brindada por OpenAI para realizar una API. Para obtener una Key [en este enlace](https://platform.openai.com/account/api-keys)

```python
# Archivo api>secret_key.py
API_KEY = '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'
```

En el archivo de "views" en nuestra aplicación "api" realizamos las importaciones necesarias para realizar el post. 

```python
# Archivo api>views.py

# Modulo para realizar la clase con las peticiones.
from django.views import View

# Modulo para retornar una respuesta en formato JSON.
from django.http.response import JsonResponse

# Modulo con nuestro modelo con el que almacenamos en nuestra base de datos la pregunta realizada y la respuesta.
from .models import Information

# Modulos para evitar el error de csrf
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

# LLave generada por OpenAI para realizar nuestra API.
import openai 
from .secret_key import API_KEY
openai.api_key = API_KEY

```

Ahora realizamos el dispatch para evitar error de csrf.
```python
# Archivo api>views.py

# Codigo que se ejecuta cada vez que realizamos/enviamos/despachemos una petición.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
```

Metodo POST que genera nuestra respuesta generada por OpenAI. Támbien almacena en nuestra base de datos un modelo "Information" que contendrá la pregunta y la respuesta para realizar un historial. 
```python
def post(self, request):
    # try catch en caso de error inesperado
    try:
        # Obtenemos los paremetros enviados (pregunta/prompt)
        json_data = json.loads(request.body)
        # Convertimos a string
        prompt = str(json_data['question'])

        # Generamos la respuesta de OpenAI
        response = openai.ChatCompletion.create(
            # Usamos el modelo gpt-3.5-turbo
            model="gpt-3.5-turbo", 
            # Mandamos la pregunta
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        # Almacenamos la respuesta como string
        prompt_answer = str(response.choices[0].message['content'])
            
        # Almacenamiento de pregunta y respuesta usando el modelo en nuestra base de datos MySQL
        Information.objects.create(question=prompt, answer=prompt_answer)
        # Almacenamos en variable "datos".
        datos = {'message': "Success", 'answer': prompt_answer}
    except:
        # En caso de error
        datos = {'message': "Unexpected Error", 'answer': "Error"}
    # Retornamos en formato JSON.
    return JsonResponse(datos)
```

Metodo GET que retorna todas las preguntas con su respectiva respuestas hechas con anterioridad por el usuario. Estas son obtenidas por medio del modelo creado en Django. Se almacenan en MySQL.
```python
def get(self, request):
    # try catch en caso de error inesperado
    try:
        # Obtenemos la lista de preguntas y respuestas por medio del modelo de Django
        informations = list(Information.objects.values())
        # Evaluamos si tiene algun dato dentro de la lista, en dado caso no tenga, retornamos una lista vacía.
        if len(informations)>0:
            datos = {'message': "Success", 'informations': informations}
        else:
            datos = {'message': "Informations not found.", 'informations': []}
    except:
        datos = {'message': "Unexpected Error", 'informations': []}
    # Retorno de datos en formato JSON.
    return JsonResponse(datos)
```





















