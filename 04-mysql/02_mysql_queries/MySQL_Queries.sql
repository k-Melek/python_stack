-- Query = Question  = ask for sth

-- CRUD  : describes Everything we can do with data Ever

-- CRUD is acronym stands for : CREATE READ UPDATE DELETE


-- ! CREATE
-- - SQL Command : INSERT

-- SYNTAX :  INSERT INTO table_name (column_name_1,column_name_2) VALUES (value_1, values_2);

-- INSERT One
INSERT INTO users (first_name, last_name, email, password) VALUES ('John', 'Wick', 'john@email.com', "112233455");

-- INSERT MANY
INSERT INTO users (first_name, last_name, email, password) VALUES ('Alex', 'Smith', 'alex@email.com', "165651515"),
('Alice', 'Jones', 'alice@email.com', "116516515"), ('Daniel', 'Wick', 'dan@email.com', "9849848"), 
('James', 'Wick', 'jamex@email.com', "112233455");

-- ! READ
-- - SQL Command : SELECT

-- SYNTAX  :  SELECT column_name_1 , column_name_2 FROM table_name ;
-- SYNTAX  :  SELECT * FROM table_name ;
-- SYNTAX  :  SELECT * FROM table_name WHERE condition;

SELECT * FROM users;

SELECT * FROM users WHERE last_name = "Wick";
SELECT * FROM users WHERE first_name LIKE "J%";

SELECT first_name, last_name FROM  users WHERE id = 2;

SELECT * FROM users ORDER BY first_name ; 
SELECT * FROM users ORDER BY first_name ASC;

SELECT * FROM users ORDER BY first_name DESC;

SELECT * FROM users  ORDER BY id LIMIT 2;


-- ! UPDATE 
-- - SQL Command  : UPDATE

-- SYNTAX  :  UPDATE table_name   SET column_name_1 = new_value2 , column_name_2 = new_value2 WHERE condition;

UPDATE user SET first_name = 'test', last_name = 'test' WHERE id = 3;

-- ! DELETE 
-- -- SQL Command : DELETE

--  SYNTAX : DELETE FROM table_name WHERE condition

DELETE FROM users WHERE id = 2;
DELETE * FROM users;



INSERT INTO addresses (user_id, street, city, zip_code) VALUES (1,'John Street', 'Compton', '6155');

SELECT * FROM users JOIN adresses ON users.id = adresses.user_id;
 
INSERT INTO products (name, price, description) VALUES ("IPHONE", 1100.50, "Very good phone"), 
("T-shirt", 15.00, "Red polo"), ("TV", 2000.50, "SMart TV");