# Тестовое задание, проект доступен по адресу : 
# http://51.250.100.64/item/1/ 
# http://51.250.100.64/buy/1/ 
# http://51.250.100.64/order/1/
# http://51.250.100.64/buy-order/1/
# http://51.250.100.64/admin - админ панель (логин:admin, пароль:admin, все модели добавлены для создания и редактирования)

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
1. GET /buy/{id} - полученный от Stripe session.id для выбранного Item выдается в результате запроса
2. GET /item/{id} - HTML страница, с информацией о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}
3. GET /order/{id} - HTML страница, с информацией о выбранном Order(На страницу также выводится список всех Item в Order и применяются Discount и Tax) и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy-order/{id}
4. GET /buy-order/{id} - полученный от Stripe session.id для выбранного Order выдается в результате запроса
