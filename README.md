# MatchPC 💻
Este un proyecto realizado por estudiantes de la Universidad del Valle de Guatemala, para la clase de Algoritmos y Estructura de Datos.
Los creadores de esta aplicacion: Walter S., Javier C. y Jose G.
Esto es el algoritmo de una aplicacion de recomendaciones para estudiantes que tienen dificultades de elegir una computadora que se adapte a sus necesidades académicas o profesionales, por el cual, por medio de ciertos datos introducidos por el usuario se le será recomendado un listado de computadoras.

## Instalación 
### Dependencias
* Descargar la última versión de [python](https://www.python.org/downloads/)
* Descargar la última versiónd de [neo4j](https://neo4j.com/download/) desktop
* Importar el framework Django desde la terminal
```
pip install django
```
* Descargar el módulo de Neo4j para python
```
pip install neo4j
```
### Set Up
Abrir Neo4j Desktop y crear una nueva base de datos con las siguientes credenciales:

Usuario  | Contraseña
------------- | -------------
neo4j | Lisp1234

Si desea cambiar estas credenciales al crear su base de datos, debera de modificar el [usuario](https://github.com/wsaldana/MatchPC/blob/master/website/website/views.py#L62) y la [contraseña](https://github.com/wsaldana/MatchPC/blob/master/website/website/views.py#L63) en la clase [Graph_manager](https://github.com/wsaldana/MatchPC/blob/master/website/website/views.py#L57)

Para cargar la base de datos inicial debera de colocar este [TEXTO](https://github.com/wsaldana/MatchPC/blob/master/website/InitialDataBase.txt) dentro la terminal de neo4j desktop y luego darle ejecutar o "run". Note que para esto deberá de iniciar la base de datos antes y luego abrirla.

Entrar al directorio [raíz](https://github.com/wsaldana/MatchPC/tree/master/website) del proyecto de django
Abrir la terminal dentro de esa carpeta
ingresar el siguiente comando:
```
python manage.py runserver
```
!Y listo! La aplicación deberá de mostrarse én el port 8000 de su localhost. Para esto ingrese dentro de su navegador:
```
localhost:8000
```

