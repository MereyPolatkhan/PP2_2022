create database PhoneBook;

create role pp2_user with password 'pp2' login;

-- alter role pp2_user login

grant all privileges on database PhoneBook to pp2_user;
-- here PROBLEM: why phonebooks is in postgres, not in PhoneBook


-- creating the table
-- name, email, number, company
create table phone_book (
    id serial not null ,
    name text not null ,
    email text,
    number numeric,
    company text
);

-- adding data to our table
insert into phone_book (id, name, email, number, company)
values (1, 'contact 1', 'contact1@gmail.com', '87078622890', 'Google');


insert into phone_book (name, email, number, company)
values ('contact 2', 'contact2@gmail.com', '87078622891', 'Netflix');

insert into phone_book (name, email, number, company)
values ('contact 3', 'contact3@gmail.com', '87078622893', 'Oracle'),
       ('contact 4', 'contact4@gmail.com', '87078622894', 'Meta');

delete from phone_book where id = 2 and company = 'Oracle';

update phone_book
set id = 2
where company = 'Netflix';

select * from phone_book
order by id asc;



-- delete table
drop table if exists phone_book;


-- Lab10 --> 1 task

-- 1) Design tables for PhoneBook
create table phonebooks (
    id serial not null ,
    name text not null ,
    email text not null,
    number text not null,
    company text not null
);

-- 2) 1) entering user name, phone from console
insert into phonebooks (name, email, number, company)
values ('contact 1', 'contact1@gmail.com', '87078622890', 'Google'),
        ('contact 2', 'contact2@gmail.com', '87078622892', 'Meta'),
        ('contact 3', 'contact3@gmail.com', '87078622893', 'Oracle'),
        ('contact 4', 'contact4@gmail.com', '87078622894', 'Linkedin'),
        ('contact 5', 'contact5@gmail.com', '87078622895', 'Amazon');

select * from phonebooks;

-- 2) 2) 1-variant upload data from csv file
copy phonebooks(id, name, email, number, company)
from 'C:\Users\USER\Desktop\coding\PP2\10_lab\1\new_contacts.csv'
delimiter ','
csv header;

-- 2) 2) 2-variant we can upload via 'import Data from File...'
-- 2) 2) 3-variant --> psql terminal --> \copy phonebooks from 'C:\Users\USER\Desktop\coding\PP2\10_lab\1\new_contacts.csv' csv;


-- 3) Implement updating data in the table (change user first name or phone)
update phonebooks
    set name = 'Merey Polatkhan'
    where id = 1;

update phonebooks
    set email = 'polatkhanmerey@gmail.com'
    where name = 'Merey Polatkhan';

update phonebooks
    set company = 'Apple'
    where id = 2;

update phonebooks
    set company = '87775557755'
    where id = 6;

update phonebooks
    set company = 'Netflix'
    where email = 'contact12@gmail.com';



-- 4) Querying data from the tables (with different filters)
select * from phonebooks
    where company in ('Meta', 'Apple', 'Amazon', 'Netflix', 'Google')
    order by id asc;

select company from phonebooks
    order by id desc;

select name from phonebooks
    where id in (1, 2, 3, 4, 5, 15);


-- 5) Implement deleting data from tables by username of phone
delete from phonebooks
    where id >= 6 and id <= 15;

delete from phonebooks
    where name in ('contact 6', 'contact 9', 'contact 12')

