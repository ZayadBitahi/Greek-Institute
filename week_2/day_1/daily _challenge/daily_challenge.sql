CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);


INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
     ('Angelina', 'Jolie', '06/05/1961', 3 ),
     ('Jennifer', 'Lopez', '11/08/1965', 3 );

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Zineb', 'BITAHI', '09/23/2000', 0);


SELECT * FROM actors;

SELECT COUNT(*) FROM actors;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Zayad', 'BITAHI', , 0);
-- Error, becuase age value cannot be NULL


SELECT avg(number_oscars) AS avergae_number_of_oscars
FROM actors;

SELECT DISTINCT number_oscars FROM actors;

SELECT * FROM actors
WHERE age > '01/01/1970';

SELECT * FROM actors
WHERE first_name IN ('David', 'Morgan', 'Will');


SELECT number_oscars, COUNT(*) as actor_count
FROM actors
GROUP BY number_oscars
HAVING number_oscars> 0 ;