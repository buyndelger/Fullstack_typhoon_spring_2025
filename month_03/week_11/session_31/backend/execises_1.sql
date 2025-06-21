-- exercise 01.1
select *from film ;
--1.2
select first_name , last_name from customer;
--1.3
select title, release_year, rental_rate from film;
 

--- exercise 02.1
select first_name "First Name" ,last_name "Last Name"
FROM
    customer; 
--2.2
select 
  title AS "Movie Title", 
    length AS "Duration (minutes)", 
    rental_rate AS "Price"
FROM 
    film;
--2.3
SELECT 
    first_name AS "Actor First Name", 
    last_name AS "Actor Last Name"
FROM 
    actor;



--exercises 3.1
select  distinct
rating
from
film;
--exercises 3.2
select  distinct
release_year
from
film;
--exercises 3.3

select  distinct
rental_rate
from
film;

--exercisi 3.4 
select distinct 
rating, release_year
from
film;
--exercises 4
SELECT *
FROM film
ORDER BY title ASC;