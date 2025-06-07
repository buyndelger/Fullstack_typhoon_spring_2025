-- aggregation function (Group By)


select
   -- distinct
   customer_id
from
   payment
group by
   customer_id
order by
   customer_id;

-- aggregation function (SUM)

select
   customer_id,
   SUM(amount) as summe
from
   payment
group by
   customer_id
order by
   summe asc;

-- LIMIT
-- which customer paid the most?
select
   customer_id,
   SUM(amount) as summe
from
   payment
group by
   customer_id
order by
   summe desc
limit 1;


-- JOIN

select
   p.customer_id,
   c.first_name,
   c.last_name,
   SUM(amount) as summe
from
   payment p
left join
   customer c
on
   c.customer_id = p.customer_id
group by
   p.customer_id,
   c.first_name,
   c.last_name
order by
   summe desc
limit 1;

-- count of customers
select count(*) from customer;

-- count of payments
select count (*) from payment;

-- count of staff
select count (*) from staff;

select  
staff_id,
count(payment_id)
from
payment
group by 
staff_id;

select 
     payment_date::date payment_date,
     sum(amount)
from 
     payment
group by 
     payment_date::date
order by 
     payment_date desc;

select 
customer_id,
SUM (amount) amount
from 
payment 
group by
customer_id 
having 
sum(amount)>200
order by 
amount desc;

select 
store_id,
count (customer_id)
from 
customer
group by 
store_id 
having
count (customer_id)>300;

drop table if exists sales;

create table sales(
brand varchar not null,
segment varchar not null,
quantity int not null,
primary key (brand,segment)
);

insert into sales (brand, segment, quantity)
values 
('ABC', 'Premium', 100),
('ABC', 'Basic', 200),
('XYZ', 'Premium', 100),
('XYZ', 'Basic', 300),
returning *;
select 
brand,
segment,
sum(quantity)
from 
sales 
gruop by 
 groping sets(
		(brand,segment),
		(brand),
		(segment),
		()
 );


