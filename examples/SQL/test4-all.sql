CREATE SCHEMA AUTHORIZATION JOHNL
CREATE TABLE Foods(
	name CHAR(8) NOT NULL,
	type CHAR(5),
	flavor CHAR(6),
	PRIMARY KEY (name)
)

SELECT Foods.name, Foods.flavor from Foods WHERE Foods.type = "fruit";

create table Cliente(
	Dni VARCHAR(10),
	Nombre VARCHAR(10),
	Apellido VARCHAR(10),
	PRIMARY KEY (Dni)
)ENGINE=InnoDB;

INSERT INTO Cliente VALUES ("721436","maoaiz",'Mauricio Aizaga');