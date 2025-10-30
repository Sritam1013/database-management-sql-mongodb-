CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  course VARCHAR(50)
);

INSERT INTO students (name, age, course)
VALUES ('John Doe', 20, 'Computer Science');
