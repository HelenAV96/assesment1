-- Database: assessmentdb

-- DROP DATABASE IF EXISTS assessmentdb;

CREATE DATABASE assessmentdb
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Swedish_Sweden.1252'
    LC_CTYPE = 'Swedish_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
--1.6	
SELECT * FROM contact_types
WHERE id NOT IN (SELECT contact_type_id
				 FROM items);
				 
--1.7			 
				 
CREATE VIEW view_contacts AS SELECT co.first_name,
co.last_name, it.contact, ct.contact_type, cc.contact_category
from items it
inner join contact_categories cc on it.contact_category_id = cc.id
inner join contact_types ct on it.contact_type_id = ct.id
inner join contacts co on it.contact_id = co.id;

--1.8

SELECT* FROM items it
FULL JOIN contact_categories cc on it.contact_category_id = cc.id
FULL JOIN contact_types ct on it.contact_type_id = ct.id
FULL JOIN contacts co on it.contact_id = co.id;