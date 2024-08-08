![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-D82C20?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-003545?style=for-the-badge&logo=sqlalchemy)
![Alembic](https://img.shields.io/badge/Alembic-336791?style=for-the-badge)
![Pydantic](https://img.shields.io/badge/Pydantic-2D3748?style=for-the-badge&logo=pydantic)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

![Prometheus](https://img.shields.io/badge/Prometheus-000000?style=for-the-badge&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)



<p align="center">
  <img src="https://github.com/user-attachments/assets/d7febe57-c66b-460e-ad9a-c9d4c4432fb4" alt="мем">
</p>

# Оглавление

- [Описание проекта](#описание-проекта)
- [Технологии](#технологии)
- [Установка и запуск](#Установка-и-запуск)
- [Конфигурация](#конфигурация)
- [API Endpoints](#API-Endpoints)
- [Документация API](#Документация-API)
- [Тестирование](#Тестирование)

# Описание проекта

API для бизнеса по выгулу собак, которое позволяет создавать заказы на выгул собак на определенное время и
просматривать список уже созданных заказов на выбранный день.

Проект состоит из 5 сервисов:

1) Публичный API с бизнес-логикой;
2) Postgresql для хранения данных заказов;
3) Redis для кеширования данных;
4) Prometheus для сбора метрик работы приложения;
5) Grafana для визуализации метрик Prometheus.

# Технологии

- **FastAPI** - используется для создания REST API. FastAPI поддерживает асинхронную обработку запросов и
  автоматическую генерацию документации.

- **SQLAlchemy** - ORM, позволяющая взаимодействовать с базой данных с использованием объектно-ориентированного
  подхода. Упрощает выполнение операций с базой данных. Используется асинхронная версия (asyncpg)

- **PostgreSQL** - объектно-реляционная система управления базами данных, используемая для хранения данных о
  заказах.

- **Pydantic** - используется для валидации и управления данными с использованием аннотаций типов Python.
  Обеспечивает строгую типизацию и валидацию входящих данных для API.

- **Redis** - система управления базами данных в памяти, используемая для кэширования данных, чтобы ускорить
  загрузку часто запрашиваемой информации.

- **Docker** - используется для запуска приложений в контейнерах. Упрощает развертывание и управление приложением,
  обеспечивая его изоляцию от окружения.

- **Docker Compose** - используется для запуска всех сервисов проекта удобным способом.

- **Alembic** - инструмент для создания миграций баз данных, позволяющий версионировать и применять изменения в схеме
  базы данных.

- **Pytest** - фреймворк для написания и выполнения тестов. Используется для тестирования приложения.

- **Admin Panel** - интерфейс администратора, обеспечивающий удобное управление данными sql хранилища.

- **Prometheus** - система мониторинга и оповещения, используется для наблюдения за работой приложения в
  реальном времени (сбор метрик).

- **Grafana** - инструмент для визуализации и анализа данных, используется для мониторинга
  производительности приложений и систем, по средствам создания информативного дашборда (использует метрики, снятые
  Prometheus).

# Установка и запуск

1. Клонируйте репозиторий:

```plaintext
   https://github.com/BogdanStitchy/Api-walking-dog.git
```

2. Перейдите в директорию проекта:

```plaintext
   cd Api-walking-dog
```

3. Для возможности запуска и проверки всех сервисов без самостоятельного создания .env файлов, .env файлы, необходимые
   для сборки и работы
   docker-compose, добавлены в корень проекта. Необходимо выполнить команды:

```bash
  docker compose build
  ```

  ```bash
  docker compose up
  ```

После запуска, приложение будет доступно по адресу: **http://127.0.0.1:9001/docs**

Админ панель для публичного сервиса: **http://127.0.0.1:9001/admin**

Prometheus будет доступен по адресу **http://127.0.0.1:9090/**

Grafana будет доступно по адресу **http://127.0.0.1:3000/**

# Конфигурация

## Публичный сервис

Расположение конфигурационного файла публичного сервиса: *config/.env*.
Содержимое файла *config/.env* следующее:

  ```dotenv
MODE=
LOG_LEVEL=
LOGIN_DB=
PASSWORD_DB=
NAME_DB=
HOST_DB=
PORT_DB=
DIALECT_DB=
DRIVER_DB=

TEST_LOGIN_DB=
TEST_PASSWORD_DB=
TEST_NAME_DB=
TEST_HOST_DB=
TEST_PORT_DB=

HOST_REDIS=

  
  ```

Файл заполняется без кавычек. В конце обязательно должна быть пустая строка.

* MODE - режим работы приложения. Доступны следующие варианты: "DEV", "TEST", "PROD"
* LOG_LEVEL - уровень логирования приложения по умолчанию
* LOGIN_DB - логин для базы данных
* PASSWORD_DB - пароль для базы данных
* NAME_DB - имя используемой базы данных
* HOST_DB - хост на котором расположена используемая база данных
* PORT_DB - порт для подключения на хосте для базы данных
* DIALECT_DB - используемая СУБД. Для выбора возможных вариантов
  ознакомьтесь с [документацией](https://docs.sqlalchemy.org/en/20/core/engines.html)
* DRIVER_DB - драйвер для СУБД. Для выбора возможных вариантов
  ознакомьтесь с [документацией](https://docs.sqlalchemy.org/en/20/core/engines.html)


* TEST_LOGIN_DB - логин тестовой базы данных
* TEST_PASSWORD_DB - пароль тестовой базы данных
* TEST_NAME_DB - имя тестовой базы данных
* TEST_HOST_DB - хост на котором расположена тестовая базы данных
* TEST_PORT_DB - порт для подключения на хосте для тестовой базы данных


* HOST_REDIS - хост расположения redis

## Внутренние параметры системы

Расположение конфигурационного файла параметров системы: *app/orders/config_orders.py*.
Содержимое файла *app/orders/config_orders.py* следующее:

```dotenv
COUNT_WALKER =
START_WALK_TIME =
END_WALK_TIME =
WALK_DURATION_MINUTES =
POSSIBLE_WALKING_TIME =
```

* COUNT_WALKER: int - количество людей, способных выгуливать питомцев (максимальное количество заказов в один временной
слот)
* START_WALK_TIME: datetime.time - время начала приема заказов на выгул в день
* END_WALK_TIME: datetime.time - время окончания приема заказов на выгул в день
* WALK_DURATION_MINUTES: int - максимальная длительность одной прогулки
* POSSIBLE_WALKING_TIME: list - возможные доступные слоты на день
(рассчитывается динамически на основе выше указанных параметров)

## Конфигурация docker compose

Переменные все те же, что и в файле *config/.env*, за исключением следующих переменных:

* POSTGRES_DB - название базы данных, созданной в docker compose
* POSTGRES_USER - логин базы данных, созданной в docker compose
* POSTGRES_PASSWORD - пароль базы данных, созданной в docker compose

# API Endpoints

### Описание эндпоинтов

1) **`GET /orders`** - Получение списка заказов на прогулку для указанной даты. Кэширование результата на 45 секунд.
   - **Параметры:** `walk_date` (date): Дата, для которой нужно получить список заказов.
   - **Ответ:** Возвращает список заказов с информацией об id заказа, номере квартиры, имени питомца, породе, времени и
     дате прогулки.


2) **`POST /orders/add_order`** - Оформление нового заказа на прогулку.
    - **Параметры:**
        - `apartment_number` (int): Номер квартиры владельца питомца;
        - `pet_name` (str): Имя питомца;
        - `pet_breed` (str): Порода питомца;
        - `walk_date` (date): Дата прогулки;
        - `walk_time` (time): Время начала прогулки (валидируется на соответствие допустимым временным интервалам);
    - **Ответ:** В случае успешного добавления возвращает статус код 201. Если выбранное время занято, возвращает
      статус код 409 и доступные интервалы для прогулок.


3) **`DELETE /orders/{order_id}`** - Удаление существующего заказа на прогулку по его ID.
    - **Параметры:** `order_id` (int): Идентификатор заказа, который нужно удалить.
    - **Ответ:** В случае успешного удаления возвращает статус код 204.


4) `GET /metrics` - Получение метрик (дефолтный эндпоинт Prometheus).

# Документация API

После запуска приложения документация API будет доступна по адресу **http://127.0.0.1/:9001/docs.**

# Тестирование

Установите все необходимые зависимости (находясь в корневой директории проекта):

```bash
pip install -r requirements.txt
```

Для запуска тестов в Bash выполните команды (находясь в корневой директории проекта):

* для запуска dao тестов сервиса:

```bash
pytest -v -s -p no:warnings app/tests/integration_tests/dao_test.py
```

* для запуска api тестов сервиса:

```bash
pytest -v -s -p no:warnings app/tests/integration_tests/api_test.py
```
