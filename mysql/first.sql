CREATE DATABASE school;

USE school;

CREATE TABLE student(
Sid INT(5),
Sname VARCHAR(50),
Smobile INT(10),
Sdept_id INT(5),
Sadd VARCHAR(50)
);

ALTER TABLE student
MODIFY Sid INT(5) UNIQUE;

ALTER TABLE student DROP PRIMARY KEY;

ALTER TABLE student
MODIFY Sid INT(5) PRIMARY KEY;

INSERT INTO student
VALUE (1,"harshit",756888888,2,"pune");

ALTER TABLE student
MODIFY Smobile INT(11) not null; 

ALTER TABLE student
MODIFY Sid INT UNIQUE; 

ALTER TABLE student
ADD grade VARCHAR(2);

UPDATE student
SET grade="A"
WHERE Sid=1;

INSERT INTO student
VALUE (2,"harsh",756888889,3,"mumbai","B");

INSERT INTO student
VALUE (3,"rishit",756888887,2,"jalandhar","C");

INSERT INTO student
VALUE (4,"hitesh",756888886,4,"banglore","A");

INSERT INTO student
VALUE (5,"kshitij",756888885,1,"pune","B");

INSERT INTO student
VALUE (6,"abhijit",756888884,3,"mumbai","A");

INSERT INTO student
VALUE (7,"abhi",756888883,3,"banglore","B");

SELECT * FROM student;

SELECT * FROM student 
WHERE grade="A";

SELECT Sadd,count(Sname) FROM student
GROUP BY Sadd;

SELECT Sid,Sadd,Smobile FROM student
ORDER BY Sadd DESC;

DELETE FROM student
WHERE Sid=7;

CREATE TABLE department(
dept_id INT(5) ,
dept_name VARCHAR(50),
FOREIGN KEY(dept_id) REFERENCES student(Sid));

ALTER TABLE department
MODIFY dept_id INT(5) UNIQUE NOT NULL;

DELETE FROM department
WHERE dept_id=1;

SELECT * FROM department;

DROP TABLE department;

INSERT INTO department
VALUES(1,"Computer Engineering");

INSERT INTO department
VALUES(2,"Information Technology");

INSERT INTO department
VALUES(3,"EnTC");

INSERT INTO department
VALUES(4,"Biotech");

SELECT * FROM student 
LEFT JOIN department 
ON student.Sdept_id=department.dept_id;

SELECT * FROM student 
RIGHT JOIN department 
ON student.Sdept_id=department.dept_id;

ALTER TABLE department
ADD teacher_name VARCHAR(50);

UPDATE department
SET teacher_name="teacher1"
WHERE dept_id=1;

UPDATE department
SET teacher_name="teacher2"
WHERE dept_id=2;

UPDATE department
SET teacher_name="teacher3"
WHERE dept_id=3;

UPDATE department
SET teacher_name="teacher4"
WHERE dept_id=4;



