#+Esto es un comentario+#
HOLA
CAROLINA
CARDONA
CREATE TABLE TIPO_USUARIO
(
idTipoUsuario int Identity(1,1),
descTipoUsuario varchar(20) NOT NULL,
CONSTRAINT PK_TIPO_USUARIO PRIMARY KEY(idTipoUsuario)
)
--esto es un comentario--
CREATE TABLE USUARIO
( #+ todo tenemos un
	amor que
	 nos complica la vida +#
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
#+Esto es un comentario+#
DROP TABLE USUARIO;
--i
INSERT INTO USUARIO (idUsuario,idTipoUsuario,apelUsuario,nomUsuario,direccion,habilitado, fechaExpCarnet,fechaVencCarnet)
VALUES ('amoros','admin','Valencia','Agustin','calle 22',1,'20-mayo-2014','20-mayo-2015');
--variable
UPDATE USUARIO
SET apelUsuario = 'Jaramillo'
WHERE nomUsuario = 'Agustin'or nomUsuario = 'robertin'
AND fechaExpCarnet = '20-mayo-2014';