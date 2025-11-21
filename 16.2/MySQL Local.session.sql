CREATE DATABASE IF NOT EXISTS company;
USE company;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
); 

DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

INSERT INTO departments (dept_name, location) VALUES
('HR', 'Hyderabad'),
('Finance', 'Mumbai'),
('IT', 'Bangalore'),
('Marketing', 'Delhi'),
('R&D', 'Chennai');

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Amit', 'Sharma', 'HR', 45000, '2020-05-20'),
('Priya', 'Patel', 'Finance', 60000, '2021-02-10'),
('Ravi', 'Kumar', 'IT', 55000, '2019-08-14'),
('Neha', 'Reddy', 'Marketing', 48000, '2022-01-05'),
('Arjun', 'Singh', 'IT', 62000, '2020-09-12'),
('Sonia', 'Verma', 'Finance', 70000, '2021-06-01');

SELECT * FROM employees;
SELECT first_name, last_name, department FROM employees;
SELECT DISTINCT department FROM employees;
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'IT';
SELECT * FROM employees WHERE hire_date > '2020-12-31';
SELECT * FROM employees ORDER BY salary ASC;
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;
SELECT COUNT(*) AS total_employees FROM employees;
SELECT AVG(salary) AS average_salary FROM employees;
SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employees;
SELECT department, SUM(salary) AS total_expenditure FROM employees GROUP BY department;
SELECT department FROM employees GROUP BY department HAVING COUNT(*) > 1;
SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department;
SELECT YEAR(hire_date) AS hire_year, COUNT(*) AS employees_hired FROM employees GROUP BY hire_year ORDER BY hire_year;
SELECT e.first_name, e.last_name, e.department, d.location FROM employees e JOIN departments d ON e.department = d.dept_name;
SELECT e.* FROM employees e JOIN departments d ON e.department = d.dept_name WHERE d.location = 'Bangalore';
SELECT * FROM employees e LEFT JOIN departments d ON e.department = d.dept_name;
SELECT d.dept_name FROM departments d LEFT JOIN employees e ON d.dept_name = e.department WHERE e.emp_id IS NULL;
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count FROM departments d LEFT JOIN employees e ON d.dept_name = e.department GROUP BY d.dept_name;
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
SELECT department FROM employees GROUP BY department ORDER BY AVG(salary) DESC LIMIT 1;
SELECT * FROM employees ORDER BY hire_date DESC LIMIT 1;
SELECT * FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;
SELECT * FROM employees WHERE department = (SELECT department FROM employees WHERE first_name = 'Amit' AND last_name = 'Sharma');
