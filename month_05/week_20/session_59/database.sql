create table Authors(
     author_id INT PRIMARY KEY,
    author_name VARCHAR(255),
    country VARCHAR(255)
);
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    publication_year INT,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);
INSERT INTO Authors (author_id, author_name, country) VALUES
(1, 'Ж.К. Роулинг', 'Их Британи'),
(2, 'Жорж Орвелл', 'Их Британи'),
(3, 'Харүки Мүраками', 'Япон');

INSERT INTO Books (book_id, title, publication_year, author_id) VALUES
(101, 'Харри Поттэр', 1997, 1),
(102, '1984', 1949, 2),
(103, 'Амьтны ферм', 1945, 2),
(104, 'Норвегийн ой', 1987, 3);


-- ex01
SELECT title, publication_year
FROM Books;

SELECT author_name
FROM Authors
WHERE country = 'Их Британи';

--ex02
SELECT title
FROM Books
WHERE publication_year IN (1945, 1997);

SELECT author_name
FROM Authors
WHERE country IN ('Их Британи', 'Япон');

--ex03
SELECT b.title, a.author_name
FROM Books b
JOIN Authors a ON b.author_id = a.author_id;

SELECT b.title, b.publication_year
FROM Books b
JOIN Authors a ON b.author_id = a.author_id
WHERE a.author_name = 'Жорж Орвелл';

--ex04
UPDATE Books
SET publication_year = 1998
WHERE title = 'Харри Поттэр';

UPDATE Authors
SET country = 'АНУ'
WHERE author_name = 'Харүки Мүраками';

--ex05
DELETE FROM Books
WHERE title = 'Амьтны ферм';
UPDATE Authors
SET country = 'АНУ'
WHERE author_name = 'Харүки Мүраками';

--ex06
INSERT INTO Authors (author_id, author_name, country)
VALUES (4, 'Стивен Кинг', 'АНУ');

INSERT INTO Books (book_id, title, publication_year, author_id)
VALUES (105, 'Дэлхийн дайн', 2023, 4);
