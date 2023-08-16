-- Creates the table id_not_null on the MySQL server
-- Does nothing if the table id_not_null already exists
CREATE TABLE IF NOT EXISTS `id_not_null` (
	`id` INT NOT NULL DEFAULT 1,
	`name` VARCHAR(256)
);
