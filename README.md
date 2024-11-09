# Древовидное меню на Django
## Stack
- Django
- SQLite3
## Описание проекта
1. Django-app реализует древовидное меню, соблюдая следующие условия:
- Меню реализовано через template tag
- Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
- Хранится в БД.
- Редактируется в стандартной админке Django
- Активный пункт меню определяется исходя из URL текущей страницы
- Меню на одной странице может быть несколько. Они определяются по названию.
- При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
- На отрисовку каждого меню требуется ровно 1 запрос к БД
2. Django-app позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
3. Используется только Django и стандартная библиотеку Python.

## Используется python=3.10

## Запуск проекта
### 1 Клонируем репозиторий

```bash
git clone https://github.com/Yomorad/django_nestedtree.git
```

### 2 Настраиваем виртуальную среду

```bash
# как пример через встроенный модуль venv из библиотеки python
python -m venv myenv
source myenv/bin/activate
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
# Приложение: http://127.0.0.1:8000
# Админка: http://127.0.0.1:8000/admin/
```

## Тест
```bash
# Переходим по http://127.0.0.1:8000/Main/
# Пример вывода:
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
