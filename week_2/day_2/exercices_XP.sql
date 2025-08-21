#exercice 1

SELECT * FROM items
ORDER BY item_price ASC;

SELECT * FROM items
WHERE item_price >= 80
ORDER BY item_price DESC;

SELECT first_name, last_name FROM customers
ORDER BY first_name ASC
LIMIT 3;

SELECT last_name FROM customers
ORDER BY last_name DESC;


#exercice 2
#1

SELECT * FROM customer;


#2

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM customer;


#3

SELECT DISTINCT create_date FROM customer;


#4

SELECT * FROM customer
ORDER BY first_name DESC;


#5

SELECT film_id, title, description,
        release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;



#6

SELECT address, phone FROM address
WHERE district = 'Texas';


#7
SELECT * FROM film
WHERE film_id = 15 or film_id = 150;

#8
SELECT film_id, title,
       description, length, rental_rate
FROM film
WHERE title = 'Arrival';

#9
SELECT film_id, title,
       description, length, rental_rate
FROM film
WHERE title ILIKE 'Ar%';

#10
SELECT title, rental_rate FROM film
ORDER BY rental_rate ASC
LIMIT 10;

#11

SELECT title, rental_rate FROM film
ORDER BY rental_rate ASC
LIMIT 10 OFFSET 10;

#12

SELECT customer.first_name, customer.last_name,
    payment.amount, payment.payment_date
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id
ORDER BY customer.customer_id;

#13


SELECT film.title, COUNT(inventory.inventory_id) AS amount_available FROM film
LEFT JOIN  inventory
ON film.film_id = inventory.film_id
GROUP BY film.title;

#14

SELECT city.city, country.country FROM city
INNER JOIN country
ON city.country_id = country.country_id
ORDER BY country.country, city.city;




