#Exercice 1 :
#1

SELECT name FROM language;



#2

 SELECT film.title, film.description, language.name
 FROM film
 LEFT JOIN LANGUAGE
 ON film.language_id = language.language_id;



#3

 SELECT film.title, film.description, language.name
 FROM film
 RIGHT JOIN LANGUAGE
 ON film.language_id = language.language_id;



 #4

 CREATE TABLE new_film(
    id SERIAL PRIMARY KEY,
    name VARCHAR (50) NOT NULL
 );

 INSERT INTO new_film (name)
 VALUES 
    ('Jurassic world'),
    ('Arrival'),
    ('Sinners');

SELECT * FROM new_film;


#5

CREATE TABLE customer_review(
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR (50) NOT NULL,
    score INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update DATE DEFAULT CURRENT_DATE
)

#6

INSERT INTO customer_review(film_id, language_id, title, score, review_text)
VALUES
    (1, 1, 'Dino Adventure', 8, 'Jurassic World is thrilling and action-packed. The dinosaurs are lifelike, and the suspense keeps you on the edge of your seat from start to finish.'),
    (2, 1, 'Thought-Provoking Sci-Fi', 9, 'Arrival is a beautifully crafted sci-fi story. The concept of language and communication with aliens is fascinating, and Amy Adams delivers a brilliant performance.'),
    (3,1,'Dark and Intense',7,'Sinners is a gripping drama with complex characters. The plot keeps you engaged, though some parts feel a bit heavy and slow at times.');

SELECT * FROM customer_review;


#7


DELETE FROM new_film WHERE name = 'Sinners';

-- The review related to the movie named Sinners is also removed. --

SELECT * FROM customer_review;




#Exercice 2 :


#1

UPDATE film
SET language_id = 2
WHERE film_id IN (1, 2, 3);

#2

-- store_id → references store.store_id
-- address_id → references address.address_id
-- Effect on INSERT: you cannot insert a customer unless the store_id and address_id exist.


#3
DROP TABLE customer_review;
-- Yes, if no other table references it. If referenced, drop the foreign key first.


#4

SELECT COUNT(*) 
FROM rental 
WHERE return_date IS NULL;


#5

SELECT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;


#6

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
  AND f.description ILIKE '%sumo%';

#6b
SELECT title
FROM film
WHERE length < 60 AND rating = 'R'
  AND description ILIKE '%documentary%';


#6c
SELECT f.title
FROM payment p
JOIN rental r ON p.rental_id = r.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON p.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND p.amount > 4.00
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';


#6d
SELECT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;