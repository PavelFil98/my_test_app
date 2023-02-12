# Тестовое задание, проект доступен по адресу : http://51.250.100.64/item/1/


### Для для запуска:
1.
```bash
git clone https://github.com/PavelFil98/my_test_app.git
```
2. Заполнить .env согласно файлу env.example
```bash
touch .env
nano .env 
```
3.  
```bash
cd infra
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
2. GET /item/{id} - HTML страница, с информацией о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}
3. http://51.250.100.64/admin - админ панель (логин:admin, пароль:admin)
