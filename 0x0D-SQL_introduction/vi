-- Convert hbtn_0c_0 database, first_table, and field 'name' to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- SQL to calculate average temperature (Fahrenheit) by city and order by temperature (descending)
SELECT city,
       ROUND(AVG((temperature * 9/5) + 32), 2) AS average_temperature_fahrenheit
FROM temperature_data
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
