# PinChef 👨‍🍳
Backend API RESTful for PinChef

Porque se llama PinChef?

Bueno se deriba de pinche que dicen las malas lenguas que quiere decir ayudante de cocina. 
Y de la pabra Chef que significa "cocinero".
ademas que tiene en su unicio lo de Pin que es como guardalo. similar a pinterest.

## Que es PinChef App?
Una aplicacion web que te permite seleccionar recetas de cocina y generar una lista de compras.

La idea es que selecciones que recetas quieres cocinar en la semana y que te genere una lista de compras para el supermercado.

### Ejemplo:
Seleccionas para un día de la semana
 - Lunes:
    - desayuno:
        - Chilaquiles
        - cafe con leche
    - Comida:
        - Picadillo (carne molida con papas y zanahorias)
        - Arroz blanco con chicharos
        - Sopa de fideos
        - Agua de Limon
    - Cena:
        - Pan tostado Integral con queso cottage, salmon ahumado y tomate cherry
        - Te de Manzanilla

Y así generas una lista de compras para el supermercado en base a tu selección.

la PinChef App te genera una lista de compras para el supermercado ayudandote a organizar el menu de la semana.
Estaria chido que se pueda conectar con las APIs de las tiendas para hacer la orden de compras en linea. 

Si hay dias vacios en la semana te notificara que hay que ordenar o salir a comprar 🌮 (taquitos) en el horarios o dias de la semana que no tengas seleccionado el menu para cubrir huecos y no te quedes sin alimentarte. 

Mostrarte recetas en base a tus gustos y a tu dieta.

Recomendaciones de ser fit o fat 💪 si nota que le hechas mucha crema a tus tacos 🌮.

Concejos para dieta vegetariana y vegana 🥗.

En base de tus compras puede sugerirte recetas que te puedan interesar ya que nadie va al mercado a comprar 2 papas solamente para el picadillo por ejemplo te diria si tienes papas puedes hacer estas recetas con las papas como pure de papa para tus acompñamientos en las comidas.

Generar un menu para la semana de desayuno, comida y cena basado en un presupuesto limitado.


# Docker
Primero que nada se debe buildear, y para ello lo hacemos de la siguiente manera ubicados en la raiz del proyecto
```sh
docker build -t <tag> .
```
Posterior a la construccion de la imagen ya queda 
```sh
docker run -d -p 80:80 <myimage> --env SQLALCHEMY_DATABASE_URL=<URL> <tag>
```
# TODOS

## Estructura app

Todo: Organización folder de la aplicación 🚀




folders:
<!-- PinChef API folder structure -->
- 📁 alembic
    - 📁 versions
    - 🐍 env.py
    - Readme.md
    - script.py.mako
- 📁 api
    - 🐍 main.py
    - 🐍 dependencies.py <!-- dependency -->
    - 📁 config
        - 🐍 db.py 
    - 📁 routes
        - 🐍 users.py
        - 🐍 recepies.py
        - 🐍 shopingLists.py
    - 📁 models
        - 🐍 models.py
        TODO: separarlos en uno por cada modelo
        - 🐍 user.py
        - 🐍 recepie.py
        - 🐍 shopingList.py
        - 🐍 item.py
    - 📁 schemas
        - 🐍 schemas.py
        TODO: separarlos en uno por cada modelo
        - 🐍 user.py
        - 🐍 recepie.py
        - 🐍 shopingList.py
        - 🐍 item.py

## Migraciones

conectar con **alembric** para hacer migraciones 

## Docker

buscar una mejor imagen para el proyecto

**tengo un error que marca que tengo un archivo de windows no se que sea **


## Routes
get: /api/users/  # lista de usuarios
post: /api/users/  --> crear usuario
get: /api/users/:id  --> para obtener un usuario
put: /api/users/:id  --> update
delete: /api/users/:id  --> delete user

get: /api/recepies/  # lista de recetas
post: /api/recepies/  --> crear receta
get: /api/recepies/:id  --> para obtener una receta
put: /api/recepies/:id  --> update
delete: /api/recepies/:id  --> delete recepie

get: /api/shopingLists/  # lista de listas de compras
post: /api/shopingLists/  --> crear lista de compras
get: /api/shopingLists/:id  --> para obtener una lista de compras
put: /api/shopingLists/:id  --> update
delete: /api/shopingLists/:id  --> delete shopingList


### Author: [Gerardo Alcántara](https://github.com/GeraAlcantara)


### TODO: me quede en los modelos en un solo archivo como los schemas