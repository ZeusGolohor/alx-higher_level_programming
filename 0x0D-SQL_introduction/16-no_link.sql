-- A script to get all records in the DB where name is not null
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL GROUP BY `score`, `name` ORDER BY `score` DESC;
