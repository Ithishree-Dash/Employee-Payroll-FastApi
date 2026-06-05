
CREATE DATABASE IF NOT EXISTS payroll_db;
USE payroll_db;

CREATE TABLE employees(
 id INT PRIMARY KEY,
 name VARCHAR(100),
 type VARCHAR(20),
 salary DOUBLE
);
