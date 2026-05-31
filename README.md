"""
7) FastAPI - Enunciado y estructura del proyecto

Tenemos una base de datos MySQL con la tabla Alumnos, que tiene un alumno y 3 notas.
Se piden las siguientes páginas:

1) (1.5 ptos) Sacar un listado de alumnos con todas sus notas en una tabla HTML.
   Las notas que sean menores que 5 se pondrán en rojo.
2) (1.5 ptos) Página donde se pondrá un formulario con una caja de texto que será un número.
   Al mandar el formulario se mostrará un listado de alumnos que tengan la media de las notas más alta que ese número.
3) (0.5 ptos) Página para cambiar el nombre de un alumno, se podrá hacer siempre que no tenga ninguna nota suspendida.
4) (1 pto) Página para actualizar las notas de un alumno, los alumnos se seleccionarán en un select.
5) (0.75 ptos) Página para borrar un alumno, los alumnos se seleccionarán en un select donde estarán los alumnos que tienen todo aprobado, y saldrá un mensaje en pantalla indicando que se borró el alumno.
6) (0.75 ptos) Las páginas tendrán un menú para acceder a todas ellas.
7) (0.5 ptos) Las páginas 1, 3 y 5 tendrán el fondo azul.
8) (0.5 ptos) Las páginas 2 y 4 el fondo amarillo.

Estructura de carpetas y funcionalidad:

- main.py
  - Define todas las rutas de la aplicación FastAPI.
  - Usa la clase DaoAlumnos para acceder a la base de datos.
  - Renderiza los templates HTML según la ruta.

- data/dao/dao_alumnos.py
  - Contiene la clase DaoAlumnos con todos los métodos de acceso a la tabla alumnos (listar, filtrar, cambiar nombre, actualizar notas, borrar).

- data/modelo/database.py
  - Función get_db() para obtener la conexión a la base de datos MySQL.

- static/css/
  - style.css y table.css: estilos para el menú, tablas, formularios y colores de fondo.

- templates/
  - base.html: plantilla base con el menú y bloques para el contenido y el color de fondo.
  - alumnos.html: listado de alumnos con notas (notas < 5 en rojo, fondo azul).
  - filtrar.html: formulario y resultados de alumnos con media superior a un número (fondo amarillo).
  - cambiar_nombre.html: formulario para cambiar nombre de alumnos aprobados (fondo azul).
  - actualizar_notas.html: formulario para actualizar notas de un alumno (fondo amarillo).
  - borrar.html: formulario para borrar alumnos aprobados y mensaje de confirmación (fondo azul).

Funcionalidad:
- Todas las rutas usan plantillas HTML y el menú está siempre visible.
- Los colores de fondo se asignan según el enunciado usando el atributo bgcolor en cada template.
- El acceso a la base de datos está centralizado en DaoAlumnos.
"""
