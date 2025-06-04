create database scholarship;
use scholarship;
Create table education(
roll_no int primary key,
name varchar(30),
father_name varchar(30),
age int,
percentage float,
monthly_income float
);
alter table education add column status varchar(20);
select*from education;
