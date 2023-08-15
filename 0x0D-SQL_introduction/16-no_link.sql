-- Lists all records of the table second_table of the database hbtn_0c_0
-- Does not list a row with out a name value
-- Result displays the score and the name
-- Records are listed by score in descending order
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
