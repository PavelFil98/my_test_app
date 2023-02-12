### Тестовое задание, проект доступен по адресу : http://158.160.25.198/item/1


## Для для запуска:
1.
```bash
git clone https://github.com/PavelFil98/my_app.git
```
2.
```bash
cd infra
```
3.  
```bash
docker-compose up -d --build   
```
4.
```bash
docker-compose up -d --build   
```
5. Выполнить миграции, создать суперюзера, собрать статику:
```bash 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
6. Проект доступен: http://localhost/

Эндпоинты:
1. GET /buy/{id} - полученный от Stripe session.id выдаеться в результате запроса
2. GET /item/{id} - простейая HTML страницу, с информацией о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}

3.http://localhost/admin - админ панель (логин:admin, пароль:admin)