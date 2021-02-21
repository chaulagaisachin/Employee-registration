create database edb;

use edb;

create table employee_data(
Emp_ID int primary key not null auto_increment,
Emp_Name varchar(50), Department varchar(50),
Address varchar(50),
Contact int signed,
Age int signed
);

DROP TABLE employee_data;

SELECT * FROM employee_data;
