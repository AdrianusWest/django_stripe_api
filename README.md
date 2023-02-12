# Задание:
-------
https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit#
(копия файла в формате *.odt находится в репозитории проекта)


## Установка и запуск

### Установка:
```
git clone https://github.com/AdrianusWest/django_stripe_api
cd ./django_stripe_api
make install
```

### Переменные окружения

Чтобы приложение работало, необходимо создать файл .env в корне проекта. Формат заполнения: 
```TOKEN = '<your token>'```

В файле .evn требуется заполнить STRIPE_SECRET_KEY и STRIPE_PUBLISHABLE_KEY, находящиеся в 
```https://dashboard.stripe.com/test/apikeys```, а так же перенести SECRET_KEY при деплое.

Для включения режима отладки установите для параметра DEBUG=True.

 
### Миграции

```
make migrate
```

### Запуск приложения

```
make runserver
```

***
```http://127.0.0.0:8000/``` - главная страница проекта

```http://127.0.0.1:8000/admin``` - административная панель с возможностью редактирования 
