Employee Database
					********** IMPORTANT **********
MAKE SURE YOU CREATE DATABASE WITH FOLLOWING REQUIREMENT TO MAKE SURE THAT THE CODE RUNS PROPERLY.

1. DataBase name: "edb"
2. Table name: "employee_data"
3. Hosted: "localhost"
4. Username: "root"
5. Password: "root"


Database Code:

create database edb;

use edb;

create table employee_data(
Emp_ID int primary key not null auto_increment,
Emp_Name varchar(50), Department varchar(50),
Address varchar(50),
Contact int signed,
Age int signed
);


Thank you!

