USE school;


DROP TABLE IF EXISTS student;

CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

INSERT INTO student (id, fullName, age) VALUES
(1, 'Alice Tiwa', 18),
(2, 'Brian Sango', 16),
(3, 'Clara Wambui', 20);


UPDATE student
SET age = 20
WHERE id = 2;

SELECT * FROM student;
