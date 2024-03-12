-- SQL to display top 3 cities' temperatures during July and August
SELECT city, MAX(temperature) AS max_temperature
FROM temperature_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;
