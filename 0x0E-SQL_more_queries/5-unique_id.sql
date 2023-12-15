-- A scriot to create a table
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT NOT NULL DEFAULT 1 UNIQUE,
	`name` VARCHAR(256) NOT NULL);
