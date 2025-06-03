--session_31
create table student(
	student_id serial primary key,
	first_name varchar(255),
	last_name varchar(255),
	birth_date DATE
);

--alter table
 --student id
--major

alter table student
add student_number varchar(25);

select * from student;

alter table student 
add major varchar(125);

--drop
alter table student 
add not_required integer;

alter table student 
drop column not_required;


create table dummy_table(
	id serial primary key,
	dummy_name varchar(255) 
);



drop table dummy_table;
--rename

select *from student;

alter table student 
rename student_number to student_nr;

/*
*multi line
*comment
*
*/

--truncate -delete data from dababase table

insert into student(first_name, last_name, birth_date, student_nr, major)
values ('buyndelger', 'boldbaatar', '2003-04-08', 'MR123456', 'game');

select *from student;

insert into student(first_name, last_name , birth_date, student_nr, major)
values ('Ounbold', 'baatar', '2003-04-08', 'MR12345', 'Gamer');
values ('balt', 'bold', '2000-04-08', 'MR12345', 'Gamer');

truncate table student;

drop table student; 

create table courses(
course_id serial primary  key,
course_name varchar(255),
course_duration integer
);
create table course_type(
course_type_id serial primary key,
course_type_name varchar(255)
);


--data insert onto course

insert into courses (course_name, course_duration)
values 
('Fullstach Course', 6),
('Web Course ',3),
('Fultter Mobile App course ',3),
('Ui Ux Course', 3)



insert into course_type (course_type_name)
values 
('Computer Sciene'),
('Design');
select *from course_type;

alter table courses 
add column course_type varchar(255);

update courses 
set course_type ='Computer Science'
where course_id  = 1;

update courses 
set course_type ='Computer Science'
where course_id  = 2;

update courses 
set course_type ='Computer Science'
where course_id  = 3;

update courses 
set course_type ='Design'
where course_id  = 4;



 alter table courses 
drop column course_type;

--alter table

alter table courses 
add column course_type integer

select *from courses;


alter table courses 
add foreign key(course_type)
references course_type(course_type_id);


update courses 
set course_type=1
where course_id  = 2;

update courses 
set course_type=1
where course_id  = 1;

update courses 
set course_type=1
where course_id  = 3;
update courses 
set course_type=1
where course_id  = 4;

select  *from course_type ct 





