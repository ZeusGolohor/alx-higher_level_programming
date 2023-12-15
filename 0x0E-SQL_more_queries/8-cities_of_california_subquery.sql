-- A script to select data base on a foreign key.
SELECT id, name FROM cities WHERE cities.state_id = (
	SELECT id FROM states WHERE name='California')
ORDER BY cities.id ASC;
