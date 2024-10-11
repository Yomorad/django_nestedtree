# Древовидное меню на Django

## Задача
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

## Используется
python=3.10

## Запуск проекта
### 1 Клонируем репозиторий

```bash
git clone https://github.com/Yomorad/django_nestedtree.git
```

### 2 Подтягиваем зависимости

```bash
pip install -r requirements.txt
```

### 3 Миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4 Загружаем фикстуры

```bash
python manage.py loaddata fixtures/menu_fixtures.json
```

### 5 Добавляем суперпользователя

```bash
python manage.py createsuperuser
```

### 6 Запуск сервера

```bash
python manage.py runserver
```

## Проверяем выполнение задания, открываем http://127.0.0.1:8000/Main/
Получим вывод:
```
Main
    Products
        Electronics
            Laptops
            Smartphones
        Home Appliances
            Washing Machines
            Refrigerators
    Services
        Support
        Repairs
    Contacts
    About Us
    Blog
        Tech News
        Product Reviews
```
Админка: http://127.0.0.1:8000/admin/
