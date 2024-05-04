# Модель сети по продаже электроники

## Задание

- Создайте веб-приложение с API-интерфейсом и админ-панелью.
- Создайте базу данных, используя миграции Django.

## Технические требования

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+

### Требования к реализации:

1) Необходимо реализовать модель сети по продаже электроники.
   Сеть должна представлять собой иерархическую структуру из трех уровней:

    - завод;
    - розничная сеть;
    - индивидуальный предприниматель.

      Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии).
      Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т.
      е. завод
      всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее
      уровень — 1.
2) Каждое звено сети должно обладать следующими элементами:
    - Название.
    - Контакты:
        - email,
        - страна,
        - город,
        - улица,
        - номер дома.
    - Продукты:
        - название,
        - модель,
        - дата выхода продукта на рынок.
    - Поставщик (предыдущий по иерархии объект сети).
    - Задолженность перед поставщиком в денежном выражении с точностью до копеек.
    - Время создания (заполняется автоматически при создании).

3) Сделать вывод в админ-панели созданных объектов.
    - На странице объекта сети добавить:
        - ссылку на «Поставщика»;
        - фильтр по названию города;
        - admin action, очищающий задолженность перед поставщиком у выбранных объектов.

4) Каждое звено сети должно обладать следующими элементами:
    - CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).
    - Добавить возможность фильтрации объектов по определенной стране.
5) Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

___

# Реализация

### Приложения:

1) users:  
   Приложение для пользователей. Пользователя регистрирует администратор (суперпользователь). Любые изменения 
   (редактирование и удаление) доступны только администратору (суперпользователю).
   Аутентификация пользователя реализована через simplejwt.
   