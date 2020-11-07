DROP TABLE IF EXISTS libro;
DROP TABLE IF EXISTS autor;

CREATE TABLE libro (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(45),
  editorial VARCHAR(45),
  disponible BOOLEAN,
  isbn VARCHAR(15)
);

CREATE TABLE autor (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(45),
  lang VARCHAR(15),
  edicion VARCHAR(45),
  fecha_publicacion DATE
);