CREATE DATABASE collage; 
USE collage;
CREATE TABLE student(
  id INT PRIMARY KEY,
  name VARCHAR(50)
);
INSERT INTO student
(id,name)
VALUES
(1,'Ankit Singh'),
(2,'Sonu'),
(3,'Anil'),
(4,'Suman'),
(5,'Rohit');

SELECT * FROM student;
 


