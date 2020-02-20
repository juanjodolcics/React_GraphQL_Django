Este proyecto esta realizado con **React** + **GrapQL** + **Django**.
A continuacion se presenta un manual para configurar tu entorno de desarrollo desde cero.
>_**Para gestionar los paquetes de Python, en este proyecto usamos [Anaconda](https://www.anaconda.com/).**_
>_**Para poder instalar React, en este proyecto usamos [Nodejs](https://nodejs.org/es/).**_
>_**Para gestionar los paquetes de Nodejs, en este proyecto usamos [npm](https://www.npmjs.com/).**_

# 1. Configuracion directorio `Django`
## 1.1 Entorno virtual
Lo primero que haremos es crear un entorno virtual utilizando **`Anaconda`**, en este entonrno instalaremos nuestros paquetes de forma local, y no de manera global en nuestra PC.
> A nuestro entorno lo llamaremos _`djangoenv`_, sientete libre de cambiarlo por el nombre que quieras.

Ejecutamos el siguiente comando:
``` sh
conda create --name djangoenv python = 3.8
```
Con el siguiente comando activamos nuestro entorno para trabajar sobre él:
``` bash
conda activate djangoenv
```
Y cuando quiera desactivarlo:
``` bash
conda deactivate
```
## 1.2 Instalación de **`Django`**
Dentro de nuestro nuevo entorno virtual, instalamos _`django`_ usando el siguiente comando:
``` sh
conda install -c conda-forge django
```
## 1.3 Directorio de trabajo
A diferencia de otros frameworks como Laravel, el directorio de nuestro proyecto Django no necesita estár en la carpeta `www/` de nuestro servidor **Apache**, puede crear un proyecto **Django** en el directorio que quiera, con el comando `cd` navegamos al directorio elegido:
``` bash
cd Documentos/www/
```
Creamos y accedemos a la carpeta  que va a contener todo nuestro proyecto:
``` bash
mkdir projectRGD
cd projectRGD/
```
## 1.4 Comando `git init`
En la carpeta actual escribiremos el siguiente comando, el cual nos permitira hacer un control de versiones en **`git`** de nuestro proyecto:
``` sh
git init
```
Luego manualmente creamos los archivos **`.gitignore`** y **`readme.md`**, nuestro directorio debe verse asi:
``` diff
projectRGD/
+ /* .gitignore
+ /* readme.md
```
## 1.5 Creacion del proyecto **`Django`**
Con el siguiente comando creamos un proyecto **`django`** al cual llamaremos _`project_start`_, sientete libre de llamarlo de otra forma:
``` bash
django-admin startproject project_start
```
Esto crea en el directorio una nueva carpeta llamada _`project_start`_ que contiene varios subcarpetas y archivos, se vee asi:
``` diff
projectRGD/
+ project_start/
+   project_start/
+     /* __init__.py
+     /* asgi.py
+     /* settings.py
+     /* urls.py
+     /* wsgi.py
+   /* manage.py
  /* .gitignore
  /* readme.md
```
Podra notar que hay dos carpetas llamadas _`project_start`_, la carpeta padre contendrá todas las aplicaciones de nuestro proyecto, la carpeta hijo contiene archivos de configuracion general de nuestro proyecto, si desea puede modificar el nombre de la carpeta padre, pero no modifique el nombre de la carpeta hijo, eso generaria errores.

 Con el comando _`cd`_ accedemos a la carpeta _`project_start`_ padre:
``` bash
cd project_start
```
> Recuerda que `project_start` es solo el nombre del proyecto, sientete libre de elegir el que quieras.

Ahora vemos el siguiente contenido en el directorio actual:
``` diff
project_start/
  project_start/
    /* __init__.py
    /* asgi.py
    /* settings.py
    /* urls.py
    /* wsgi.py
  /* manage.py
```
> En este punto ya podemos probar el proyecto con un **servidor de desarrollo** proporcionado por **Django**, para eso usamos en siguiente comando: **`python manage.py runserver`**.
## 1.6 Creacion de una aplicación
> ### Aplicacion vs Proyecto
> Un proyecto puede contener una o mas aplicaciones, las aplicaciones son pequeñas partes del software que esta diseñada para un uso especifico.

Crearemos una aplicacion en **Django** que contendra nuestra aplicacion **`React`**, la llamaremos _`frontend`_, usaremos el siguiente comando:
``` bash
python manage.py startapp frontend
```
Este comando creó los siguientes directorios y archivos:
``` diff
project_start/
+ frontend/
+   migrations/
+     /* __init__.py
+   /* __init__.py
+   /* admin.py
+   /* apps.py
+   /* models.py
+   /* test.py
+   /* views.py
  project_start/
    /* __init__.py
    /* asgi.py
    /* settings.py
    /* urls.py
    /* wsgi.py
  /* manage.py
```
## 1.7 Configuración básica de la aplicación _`frontend`_.
Antes de continuar, necesitamos registrar nuestra aplicacion, para eso agregamos **`'frontend.apps.FrontendConfig'`** en el array _`INSTALLED_APPS`_ que se encuentra en _`project_start/settings.py`_:
``` Python
INSTALLED_APPS = [
    'frontend.apps.FrontendConfig',
    ...
]
```
Dentro de la carpeta _`frontend/`_ crearemos las subarpetas _`static/frontend`_ y _`templates/frontend`_:
``` bash
mkdir frontend/templates/
mkdir frontend/templates/frontend/
mkdir frontend/static/
mkdir frontend/static/frontend/
```
>La carpeta _`frontend/template/frontend/`_ es la carpeta predeterminada de **`Django`** para los templates, y es donde ubicaremos nuestro _`index.html`_, que luego será el punto de partida de nuestra aplicacion **`React`**. La carpeta _`frontend/static/frontend/`_ es la carpeta predeterminada de **`Django`** para los archivos estaticos(imagenes, scripts, hojas de estilo).

Creamos un archivo **`index.html`** en _`frontend/template/frontend/`_ y escribimos el siguiente código:
``` html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>React Starter</title>
</head>
<body>
  <h1>Hola Mundo!!!</h1>
</body>
</html>
```
Ahora crearemos una vista que usara el template **`index.html`** que acabamos de crear, para lograrlo abrimos el archivo _`frontend/views.py`_ y agregamos la siguiente funcion:
``` Python
from django.shortcuts import render

def index(request):
  return render(request, 'frontend/index.html')
```
El parametro  `'frontend/index.html'` en la funcion **`render`** hace referencia a _`frontend/template/frontend/index.html`_.

Ahora debemos configurar las rutas de nuestra aplicacion, para eso creamos el archivo **`urls.py`** en la carpeta _`frontend/`_ y escribiremos el siguiente codigo:
``` Python
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
]
```
Y ahora modificamos algunas lineas en el archivo **`urls.py`** de la carpeta _`project_start/`_, debe quedar asi:
``` Python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('home/', include('frontend.urls')),
    path('admin/', admin.site.urls),
]
```
Tu directorio debe verse asi:
``` diff
project_start/
  frontend/
    migrations/
      /* __init__.py
+   static/
+       frontend/
+   templates/
+       frontend/
+               /* index.html
    /* __init__.py
    /* admin.py
    /* apps.py
    /* models.py
    /* test.py
+   /* urls.py
    /* views.py
  project_start/
  /* manage.py
```
En este punto puedes ejecutar **`python manage.py runserver`** y en tu navegador acceder a [http://localhost:8000/home/](http://localhost:8000/home/).
# 2. Configuracion directorio `React`
## 2.1 Iniciando
Accedemos a la carpeta _`frontend/`_, que es el directorio donde trabajaremos con **`React`**:
``` bash
cd frontend/
```
Iniciamos el proyecto con el siguiente comando:
``` bash
npm init
```
Manualmente creamos un archivo _`.gitignore`_.
Luego creamos la siguente carpeta:
``` bash
mkdir src/
```
> La carpeta _`src/`_ contendra nuestro codigo **`.jsx`**.
## 2.2 Babel
En el terminal ejecuta el siguiente codigo:
``` bash
npm install --save-dev @babel/core @babel/cli @babel/preset-env @babel/preset-react
```
En la acrpeta actual (_`frontend/`_) cree un archivo llamado _`babel.config.json`_.
Aqui le decimos a **`Babel`** que vamos a usar preajustes **`env`** y **`react`**. Dentro del archivo escribimos: 
``` json
{
  "presets": ["@babel/env", "@babel/preset-react"]
}
```
## 2.3 Webpack
En el terminal ejecuta el siguiente codigo:
``` bash
npm install --save-dev webpack webpack-cli webpack-dev-server style-loader css-loader babel-loader
```
Cree un nuevo archivo llamado _`webpack.config.js`_. Este archivo exporta un objeto con la configuracion de webpack. En al archivo escribimos lo siguiente:
``` js
const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  mode: "development",
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel-loader",
        options: { presets: ["@babel/env"] }
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }
    ]
  },
  resolve: { extensions: ["*", ".js", ".jsx"] },
  output: {
    path: path.resolve(__dirname, "static/frontend/"),
    publicPath: "/frontend/",
    filename: "bundle.js"
  },
  devServer: {
    contentBase: path.join(__dirname, "templates/frontend/"),
    port: 3000,
    publicPath: "http://localhost:3000/script/",
    hotOnly: true
  },
  plugins: [new webpack.HotModuleReplacementPlugin()]
};
```
## 2.4 React
En el terminal ejecuta el siguiente codigo:
``` bash
npm install --save react react-dom
```
Cree un archivo index.js en la carpeta src y escriba el siguiente codigo:
``` js
import React from "react";
import ReactDOM from "react-dom";
import App from "./App.js";
ReactDOM.render(<App />, document.getElementById("root"));
```
Cree un archivo App.js en la carpeta src y escriba el siguiente codigo:
``` js
import React, { Component} from "react";
import "./App.css";
class App extends Component{
  render(){
    return(
      <div className="App">
        <h1> Hello, World! Dolci</h1>
      </div>
    );
  }
}
export default App;
```
Cree un archivo App.css en la carpeta src y escriba el siguiente codigo:
``` css
.App {
  margin: 1rem;
  font-family: Arial, Helvetica, sans-serif;
}
```
Modificamos el **`<body>`** en el archivo **`index.html`** que esta en  _`template/frontend/`_ de la siguente manera:
``` html
<body>
  <div id="root"></div>
  {% load static %}
  <script src="{% static "frontend/bundle.js" %}"></script>
</body>
```
Finalmente añadimos los scripts **`start`** y **`build`** en **`package.json`** de la siguiente manera:
``` json
{
  "scripts": {
    "start": "webpack-dev-server --mode development",
    "build": "webpack --watch --colors"
  },
}
```
Ahora ya puede ejecutar **`npm run build`** para compilar el proyecto react cada vez que se detecte un cambio. Tambien ejecute **`python manage.py runserver`** para correr el servidor de desarrollo de **Django**.











