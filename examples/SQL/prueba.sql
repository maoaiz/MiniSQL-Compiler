UPDATE USUARIO SET a="hola" WHERE b=1;
DROP TABLE USUARIO;
--esto es un comentario--
CREATE TABLE TIPO_USUARIO
(
	idTipoUsuario int Identity(1,1),
	descTipoUsuario varchar(20) NOT NULL,
	CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
CREATE TABLE TIPO_USUARIO
(
	idTipoUsuario int Identity(1,1),
	descTipoUsuario varchar(20) NOT NULL,
	CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
DROP TABLE USUARIO;
CREATE TABLE TIPO_USUARIO
(
	idTipoUsuario int Identity(1,1),
	descTipoUsuario varchar(20) NOT NULL,
	CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
CREATE TABLE TIPO_USUARIO
(
	idTipoUsuario int Identity(1,1),
	descTipoUsuario varchar(20) NOT NULL,
	CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
select * from a;
CREATE TABLE TIPO_USUARIO
(
	idTipoUsuario int Identity(1,1),
	descTipoUsuario varchar(20) NOT NULL,
	CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
CREATE TABLE TIPO_USUARIO
(
	idTipoUsuario int Identity(1,1),
	descTipoUsuario varchar(20) NOT NULL,
	CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
select nombre, apeelido,ugyt,sdfs from hola;
select nombre, apeelido,ugyt,sdfs from hola;
CREATE TABLE TIPO_USUARIO
(
	idTipoUsuario int Identity(1,1),
	descTipoUsuario varchar(20) NOT NULL,
	CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
--i
INSERT INTO USUARIO (idUsuario,idTipoUsuario,apelUsuario,nomUsuario,direccion,habilitado, fechaExpCarnet,fechaVencCarnet)
VALUES ('amoros','admin','Valencia','Agustin','calle 22',1,'20-mayo-2014','20-mayo-2015');
--variable
UPDATE USUARIO
SET apelUsuario = 'Jaramillo Okonor'
WHERE nomUsuario = 'Agustin' or nomUsuario = 'robertin' AND fechaExpCarnet ='20-mayo-2014';

CREATE TABLE USUARIO
(
	idUsuario char(8)NOT NULL,
	idTipoUsuario int NOT NULL,
	apelUsuario varchar(35)NOT NULL,
	nomUsuario varchar(35) NOT NULL,
	direccion varchar(50)NULL,
	habilitado bit NOT NULL,
	fechaExpCarnet smalldatetime NOT NULL,
	fechaVencCarnet smalldatetime NOT NULL,
	CONSTRAINT PK_USUARIO_idUsuario PRIMARY KEY(idUsuario),
	CONSTRAINT FK_USUARIO_idTipoUsuario FOREIGN KEY (idTipoUsuario) REFERENCES TIPO_USUARIO(idTipoUsuario)
)
