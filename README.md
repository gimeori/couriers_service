Задание на практику от Estesis.tech

1. Создайте в PostgreSQL базу данных couriers_service
2. Введите свои данные для авторизации базы данных postgres в файле .env
3. Введите в терминале
```
    python init_db.py
```
4. Запустите сервер FastAPI с помощью команды:
```
    uvicorn main:app --reload
```


<h1>Описание эндпоинтов</h1>
| Left-| Center Aligne| Right Aligned                                |
|:---- |:------------:| --------------------------------------------:|
|POST  | /courier     |Регистрация курьера в системе                 |
|GET   |/couriers     |Получение списка всех курьеров                |
|GET   |/courier/{id} |Получение подробной информации о курьере по id|
|POST  |/order        |Публикация заказа в системе                   |
|GET   |/order/{id}   |Получение информации о заказе                 |
|POST  |/order/{id}   |Завершение заказа                             |
|GET   | /docs/       |Документация API                              | 

| Left-Aligned  | Center Aligned    | Right Aligned                                   |
|:------------- |:-----------------:| -----------------------------------------------:|
| POST          | /courier          | Регистрация курьера в системе                   |
| GET           | /couriers         | Получение списка всех курьеров                  |
| GET           | /courier/{id}     | Получение подробной информации о курьере по id  |
| POST          | /order            | Публикация заказа в системе                     |
| GET           | /order/{id}       | Получение информации о заказе                   |
| POST          | /order/{id}       | Завершение заказа                               |
| GET           | /docs             | Документация API                                |


