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

CREATE TABLE contact_categories (
    id SERIAL NOT NULL PRIMARY KEY,
    contact_category VARCHAR(80) NOT NULL
);

CREATE TABLE contact_types (
    id SERIAL NOT NULL PRIMARY KEY,
    contact_type VARCHAR(80) NOT NULL

CREATE TABLE contacts (
    id SERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    title VARCHAR(80),
    organization VARCHAR(80)
);

CREATE TABLE items (
    contact VARCHAR(80) NOT NULL,
    contact_id integer NOT NULL,
    contact_type_id integer,
    contact_category_id integer
);
	

INSERT INTO items (
contact, contact_id, contact_type_id, contact_category_id) 
VALUES ('011-12 33 45',3,2,1),
('goran@infoab.se',3,1,2),
('010-88 55 44',4,2,2),
('erik57@hotmail.com',1,1,1)
('@annapanna99',2,4,1)
('077-563578',2,2,1)
('070-156 22 78',3,2,2)
;



INSERT INTO contact_types( contact, contact_id, contact_type_id, contact_category_id)
VALUES ('Home'), ('Work'), ('Fax');


INSERT INTO contact_categories( contact_category)
VALUES ('Home'), ('Work'), ('Fax');

INSERT INTO contacts(first_name, last_name, title, organization)
VALUES ('Erik', 'Eriksson','Teacher','Utbildning AB'),                                                                   
('Anna','Sundh', null,null),
('Ann-Marie','Bergqvist','Cousin', null),
('Herman','Appelkvist',null, null),
('Goran','Bregovic','Coach','Dalens IK';

INSERT INTO contacts(first_name, last_name, title, organization)
VALUES ('Helen', 'Albandak Vähäkangas','Data Engineer','Academic work'),                                                                   
('Henrik','Vähäkangas', 'Vakthavande Befäl','Kriminalvården');



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