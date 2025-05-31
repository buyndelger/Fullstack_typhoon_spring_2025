create table students (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birth_date DATE,
    email VARCHAR(255),
    course_name VARCHAR(255),
    grade INTEGER
);

insert into STUDENTS (first_name, last_name, birth_date, email, course_name, grade)
values('Berkh-Ochir', 'Ochirbat', '2000-01-01', 'berkhee@gmail.com', 'fullstack course', 70);

insert into STUDENTS (first_name, last_name, birth_date, email, course_name, grade)
values
('Oyunbold', 'Naranjargal', '2001-01-01', 'oyunbold@gmail.com', 'fullstack course', 90),
('Buyanaa', 'Boldbaatar', '2002-01-01', 'buyanaa@gmail.com', 'fullstack course', 80);


select  * from students; 

select * from students where first_name = 'Buyanaa';

select first_name from students where first_name ='Buyanaa';

select first_name, last_name from students where first_name ='Buyanaa';

update students set first_name = 'Buyandelger' where first_name = 'Buyanaa'


insert into students (first_name, last_name, birth_date , email, course_name, grade)
values 
('Balt', 'Batzaya', '1999-01-01', 'balt@gmail.com', 'fullstack course', 60);


delete from students where first_name = 'Balt';


create  table courses(
course_id INTEGER,
course_name VARCHAR(255)
);

select * from  courses; 

insert  into courses  (course_id ,course_name)
values 
(1, 'fullstach course'),
(2, 'fultter mobile course'),
(3, 'web font end course'),
(4, 'ui ux course');
insert  into courses  (course_id ,course_name)
values 
(5, 'kids mobile course');


create table teachers (
teacher_id SERIAl,
teacher_name VARCHAR(255),
teacher_course VARCHAR(255)
);


insert into teachers ( teacher_name ,teacher_course)
values 
('Enhjin,' ,'kids Web App'),
('Khangaikhuu', 'Fullstack Web'),
('Khongorzul', 'Web front End'),
('Dairamaa', 'Mobile App');

select *from teachers;

insert into teachers (teacher_id, teacher_name, teacher_course)
values 
(1, 'Khangaikhuu', 'Flutter Moblie app')


create table classes (
class_id SERIAL primary key,
class_name VARCHAR(255),
class_duration INT
);

insert into classes  (class_name , class_duration)
values 
('Fullstach Web COURSE', 6),
('Web Front End',3),
('Flutter Mobile', 3),
('UI/UX,',3);
select *from classes;

insert into classes (class_id, class_name, class_duration)
values 
(5, 'Kids Moblie',2);