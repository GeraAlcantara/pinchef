# PinChef 👨‍🍳
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
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

# Install & Run

Primero clonamos el repositorio ya sea en la terminal o en el boton Code.
    
```bash
git clone https://github.com/GeraAlcantara/pinchef.git
cd pinchef
```

## Modificar el archivo de configuracion .env 
Tenemos que renombrar el archivo modify_me.env a .env y modificar los valores de las variables remomoviendo los `{}`.

Terminal 

```bash
mv modify_me.env .env
```

## Dockers
Debemos tener instalado docker y docker-compose.

Terminal 
    
```bash
sudo apt-get update
sudo apt-get install docker.io
sudo apt-get install docker-compose
sudo usermod -aG docker $USER
```

## Build 

```bash
docker-compose build
```

## Run 

```bash
docker-compose up
```

## Correr el app sin Dockers

Debemos crear un virtual env y instalar las dependencias.
Utilizamos venv para crear el virtual env. 

La variable de SQLALCHEMY_DATABASE_URL se debe de cambiar a una base de datos SQLite.

`SQLALCHEMY_DATABASE_URL= sqlite:///./pinchef.db`

Para poder correrla localmente sin necesidad de una Posgres database.
    
    
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
Y para correr el app.
 
    
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
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
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://sergioribera.com/"><img src="https://avatars.githubusercontent.com/u/56278796?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sergio Alejandro Ribera Costa</b></sub></a><br /><a href="https://github.com/GeraAlcantara/pinchef/commits?author=SergioRibera" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!