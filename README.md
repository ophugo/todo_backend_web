# todo_backend_web

Una apliación django, que puede ser deployeada facilmente en Heroku.


## Correr localmente
### No es necesario instalar el backend, ya que incluso el frontend local tiene los urls del api que esta en la web.!!

Asegurar de tener Python 3.9 [instalado localmente](https://docs.python-guide.org/starting/installation/). Para hacer push a Heroku
necesitarás instalar el [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), así como [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/ophugo/todo_backend_web.git
$ cd APItodo/

$ python3 -m venv APItodo
$ pip install -r requirements.txt

$ pip install djangorestframework
$ pip install django-cors-headers 
$ pip install psycopg2-binary

$ createdb postgres

$ python manage.py migrate
$ python manage.py runserver
```

La apicación se estará corriendo en este momento en [localhost:5000](http://localhost:5000/).

## Deployear a Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deployear](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

