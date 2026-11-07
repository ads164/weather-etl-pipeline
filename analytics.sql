-- 1. Вся погода с названиями городов
SELECT
    c.city_name AS "Город",
    f.temperature_c AS "Температура, °C",
    f.humidity AS "Влажность, %",
    f.observation_time AS "Время замера"
FROM weather_facts f
JOIN dim_cities c ON f.city_id = c.city_id
ORDER BY f.observation_time DESC;

-- 2. Средняя температура по каждому городу
SELECT
    c.city_name,
    AVG(f.temperature_c) AS avg_temp
FROM weather_facts f
JOIN dim_cities c ON f.city_id = c.city_id
GROUP BY c.city_name;

-- 3. Самый ветреный город за все время
    SELECT
        c.city_name,
        f.wind_speed_kmh
    FROM weather_facts f
    JOIN dim_cities c ON f.city_id = c.city_id
    ORDER BY f.wind_speed_kmh DESC
    LIMIT 1;