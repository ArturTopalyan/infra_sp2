# infra_sp_2
### Описание
docker-compose к проекту [api_yamdb](https://github.com/ArturTopalyan/api_yamdb)
### Технологии

- Python 3.7
- Django 2.2.19
- Django REST Framework
 
### Запуск проекта в dev-режиме
- перейти в директорию infra и создать файл .env и оформить по такому образцу
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432 
```
- запустить docker-compose ```docker-compose up --build -d```
- выполнить миграции, собрать статику и создать суперпользователя
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic
docker-compose exec web python manage.py createsuperuser
```
- перезапустить docker-compose
### Автор
* [Артур Топалян](https://github.com/ArturTopalyan)
