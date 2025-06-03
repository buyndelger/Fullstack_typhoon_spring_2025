--dvd rental databse

select * from actor;  

select first_name from actor;

select first_name, last_name , email from  customer; 

SELECT
	first_name ||' '||last_name as full_name,
	email 
FROM
    customer; 


select 
first_name,
last_name as surname
from customer;


SELECT
	first_name ||' '||last_name "Full Name"
FROM
    customer; 

--FROM -> SELECT -> ORDER BY


select 
first_name,
last_name
from 
customer 
order by
first_name  asc,
last_name desc;

select 
first_name,
length(first_name) len
from 
customer 
order by 
len desc;

--DISTINCT
create table colors(
id serial primary key,
bcolor varchar,
fcolor varchar
);

insert into 
colors (bcolor ,fcolor)
values 
('red', 'red'),
('red', 'red'),
('red', NULL),
(NULL, 'red'),
(NULL, NULL),
('green', 'green'),
('blue', 'blue'),
('blue', 'blue');
select bcolor from colors;



select *from colors;

select distinct bcolor
from 
colors 
order by 
bcolor;

select distinct bcolor, fcolor 
from 
colors 
order by 
bcolor,
fcolor;



--WHERE filtering
--1
select 
last_name,
first_name
from 
customer 
where first_name ='Jamie';

--2 --AND
select 
last_name,
first_name
from 
customer 
where first_name ='Jamie'
and last_name = 'Rice';



--3 --OR

select 
first_name,
last_name
from 
customer 
where 
first_name ='Rodriquez'
or last_name = 'Adam';

--4 --IN
select 
last_name,
first_name
from 
customer 
where 
first_name in ('Ann', 'Anne', 'Annie');



--5 --LIKE
select 
first_name,
last_name
from 
customer 
where 
first_name like 'Ann%';

--6 --BETWEEN

select 
first_name,
length(first_name)name_lenght
from 
customer 
where 
first_name like 'A%'
and length(first_name) between 3
and 5 
order by name_lenght;

--<> not equal
 



