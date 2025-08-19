CREATE TABLE items(
 item_id SERIAL PRIMARY KEY,
 item_name VARCHAR (50) NOT NULL,
 item_price INTEGER NOT NULL
)

INSERT INTO items(item_name, item_price)
VALUES 
  ('Small Desk', 100),
  ('Large desk', 300),
  ('Fan', 80);


CREATE TABLE customers(
 customer_id SERIAL PRIMARY KEY,
 first_name VARCHAR(50) NOT NULL,
 last_name VARCHAR(100) NOT NULL
)

INSERT INTO customers(first_name, last_name)
VALUES 
  ('Greg', 'Jones'),
  ('Sandra', 'Jones'),
  ('Scott', 'Scott'),
  ('Trevor', 'Green'),
  ('Melanie', 'Johnson');



SELECT * FROM items
WHERE item_price > 80;

SELECT * FROM items
WHERE item_price <= 300;

SELECT * FROM customers
WHERE last_name = 'Smith';

SELECT * FROM customers
WHERE last_name = 'Jones';

SELECT *FROM customers
WHERE first_name != 'Scott';


