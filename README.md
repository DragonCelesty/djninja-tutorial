#Pasos para crear una app con django-ninja

- Agregar en el archivo requirements.txt las dependencias de Django y django-ninja
- Crear proyecto con el comando django-admin startproject <nombre_del_proyecto>
- Entrar en la carpeta del proyecto
- Crear el aplicacion que vamos a desarrollar con el comando python manage.py startapp <nombre_de_la_aplicacion>
- Agregar la aplicacion al INSTALLED_APPS en el archivo settings.py del proyecto
- En la carpeta de la nuestra aplicacion se crea el archivo api.py que contendra nuestros endpoints creados con django-ninja