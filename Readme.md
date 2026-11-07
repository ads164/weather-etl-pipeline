# Weather ETL Pipeline

Это пет-проект, в котором собран полноценный ETL-пайплайн (Extract -> Transform -> Load). Проект забирает данные о погоде из открытого API, очищает их с помощью Pandas и сохраняет в базу данных PostgreSQL.

## Стек технологий
* **Python 3.12** (requests, pandas)
* **PostgreSQL**
* **SQLAlchemy**
* **Visual Crossing API**

## Архитектура
Я постарался спроектировать базу данных по подходу **Star Schema**. Это разделяет данные на две таблицы:
* `dim_cities` — справочник городов (измерения). Здесь хранятся названия и координаты.
* `weather_facts` — таблица с фактами погоды (температура, влажность). Она связана с городами через `city_id`.

**Из чего состоит проект:**
1. `extract.py` — код, который делает запрос к API и получает сырые данные в формате JSON.
2. `transform.py` — очистка данных и приведение типов. Например, если API присылает влажность как `65.4`, скрипт безопасно округляет её до целого числа.
3. `create_table.py` — скрипт, который создаёт таблицы в базе данных.
4. `load.py` — главный скрипт, который связывает всё вместе и загружает данные в базу.
5. `analytics.sql` — несколько SQL-запросов (с JOIN и GROUP BY), которые показывают, как можно анализировать эти данные.

## Как запустить
1. Установите нужные библиотеки (я добавил файл `requirements.txt`):
   ```bash
   pip install -r requirements.txt

## Результаты

<img width="809" height="662" alt="image" src="https://github.com/user-attachments/assets/59ab4281-ed09-4d91-aabe-427cf54cd9f9" />

<img width="1170" height="418" alt="image" src="https://github.com/user-attachments/assets/023534d3-f7ae-4967-aa88-b87933087420" />

<img width="676" height="317" alt="image" src="https://github.com/user-attachments/assets/97a10176-c301-4822-a8e4-750b4062189a" />


