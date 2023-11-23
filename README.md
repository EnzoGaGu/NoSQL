# NoSQL



Proyecto final para la materia Base de datos NoSQL de la carrera Tecnólogo en Informática, hecho en Python y MongoDB.

## Tecnologías elegidas:


Elegimos MongoDB debido a que creemos que, de las opciones que tenemos disponibles, es la más accesible y a la que mayor potencial podemos exprimirle de cara a futuro. Utilizamos MongoDB Compass como interfaz gráfica y MongoDB Atlas para las conexiones en la nube.

Python, por su lado, es una tecnología accesible y con una gran compatibilidad con MongoDB, por lo que fue la opción más adecuada para esta tarea. Utilizamos pymongo para conectar ambas de manera sencilla.


## Descarga e inicialización del proyecto:


### Requisitos previos:

+ Python 3.11
+ MongoDB Compass
+ Postman
+ VS Code

### Inicialización: 

Para comenzar con la instalación, será necesario tener este repo descargado en su sistema local. Desde el CMD de Windows/Linux, se ejecuta el siguiente comando: 

> pip install pymongo

De esta manera, se instalará pymongo (librería necesaria para inicializar el proyecto). Luego, será necesario que instale la extensión de Python en VS Code. Ahora ya es posible ejecutar el proyecto y añadir, ver y filtrar datos desde la BD. 

### Configuración de MongoDB Compass:

Para ver los cambios en la BD en tiempo real, será necesario acceder a ésta utilizando MongoDB Compass. Para ello, luego de tener el programa instalado, se deberá crear una conexión utilizando el siguiente URI: 

> mongodb+srv://GuestUser:SoyUnaPass12345678@cluster0.o1jktdl.mongodb.net/

De esta manera, se iniciará sesión con un usuario genérico, permitiendo ver los datos. 

### Configuración de Postman: 

Luego de inicializar el proyecto, y habiendo instalado el programa previamente especificado, se deberá acceder al siguiente link: 

> https://www.postman.com/cloudy-meteor-237196/workspace/nosql-postmanaccess 

Y forkear las colecciones llamadas 'MongoDB Data API' y 'MongoDB Data API for Domicilios'. Ahora, podrá hacer requests de prueba directamente a la BD desde Postman. La primera colección permite trabajar con Personas, y la segunda con Domicilios. Ambas generan datos aleatorios. 
