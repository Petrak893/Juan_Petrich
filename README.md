# Proyecto Coderhouse

Comision: Coder 54135

Alumno: Juan Petrich

## Acerca de proyecto
Un blog de los x-men que sirve de enciclopedia para acceder a toda la informacion de este mundo de ficcion
## Aplicaciones
Core - Se pueden crear usuarios y se le agrego la posibilidad de subir avatar sin necesidad de administrador
----
Autores - tiene hecho su respectivo Crud
----
Peronajes - Tiene hecho el CRUD para niveles mutantes y para los personajes
### Modelos
User - Modelo de los usuarios que interactuan con la pagina
Profile - Modelo cual hereda del modelo User y se usa para guardar imagenes para el usuario
----
Autores - Modelo de escritores y dibujantes que crearon a los X-men, usa texto para nombre y biografia, fecha para el nacimiento y usa buleanos para determinar si es escritor y/o dibujante. Cuenta con imagenes
----
Nivel Mutante - Usa campos de texto para el nombre y descripcion, campo numerio para determinar el nivel, del mas debil que es el 1, hasta 6 que es mas fuerte

Personajes - Los personajes es modelo con mas campos, texto para el nombre, nombre real, poderes, descripcion. Los otros campos son edad que usa valor numerico, fecha de creacion que es el admin pueda controlar como se actualiza la lista, e imagenes
## Mejoras Futuras
Ademas de tocar el Fronted que le falta detalles y hacer cosas como que aparezcan ejemplos (Preferiblemente aleatorios) de personajes para cuando se ve el detalle de Nivel Mutante. Tambien se podria haber hecho que el nivel en Nivel Mutante solo pueda estar en el rango del 1 al 6, para no generar problems o confuciones. Crear nuevos modelos como Comics o un apartado para las Pelicuas y Series asi se hace una enciclopedia mas completa, y en lo posible con un buen flujo de navegacion. Mejorar la experiencia del usuario y darle mas apartados para personalizar su perfil. Crear cajas de texto en los distintos detalles para que los usuarios opinen y discutan sobre los personajes y autores. 

## Problemas conocidos
Ademas del Fronted he tenido problemas a la hora de hacer un request y es dificil saber si es por el from, views o las urls, o todo lo anterior junto. No me gusta como busca los disntos elementos de las lista a la hora de usar la pagina, pero eso se podria mejorar. Y nada, ademas de chocarme con varias paredes a la hora de hacer esto lo disfrute y fui aprendiendo varias cosas, y espero ver como da frutos esto para cuando me choque con las siguientes paredes sea aunque sea mas ameno, pero siempre para adelante