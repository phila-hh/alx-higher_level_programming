-- Creates the table unique_id on the MySQL server
-- Does nothing if the table unique_id already exists
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT NOT NULL DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
