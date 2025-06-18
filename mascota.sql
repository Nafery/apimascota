-- Region de creacion de tablas
CREATE TABLE usuario (
	id INT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    password VARCHAR(255),
    comuna VARCHAR(100)
);

CREATE TABLE mascota (
	id INT PRIMARY KEY,
	nombre VARCHAR(100),
    raza VARCHAR(100),
    tipo VARCHAR(100),
    edad VARCHAR(100),
    sexo VARCHAR(20),
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE consulta (
	id INT AUTO_INCREMENT PRIMARY KEY,
	tipo VARCHAR(100),
    fecha DATE,
    precio INT,
    mascota_id INT,
    FOREIGN KEY (mascota_id) references mascota(id)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Region de inserción de datos
LOAD DATA LOCAL INFILE '/Users/naferyh/Desktop/UWU/S5/BPM/usuarios_final.csv'
INTO TABLE usuario
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nombre, correo, password, comuna, id);

LOAD DATA LOCAL INFILE '/Users/naferyh/Desktop/UWU/S5/BPM/mascotas_final.csv'
INTO TABLE mascota
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nombre, raza, tipo, edad, sexo, usuario_id, id);

LOAD DATA LOCAL INFILE '/Users/naferyh/Desktop/UWU/S5/BPM/consultas_final.csv'
INTO TABLE consulta
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(tipo, fecha, precio, mascota_id);

SELECT *
FROM consulta;