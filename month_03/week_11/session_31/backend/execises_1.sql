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
SELECT DISTINCT rating
FROM film;