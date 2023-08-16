-- Creates the MySQL server user user_0d_1
-- user_0d_1 gets all privileges on the MySQL server
-- Sets user_0d_1 password to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON * . * TO 'user_0d_1'@'localhost';
