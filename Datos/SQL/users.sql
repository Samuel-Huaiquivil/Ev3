CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    nombre_usuario VARCHAR(100) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    telefono VARCHAR(100),
    web VARCHAR(255),
    compania_id INT,
    CONSTRAINT fk_usuario_compania
        FOREIGN KEY (compania_id) REFERENCES companias(id) 
        ON DELETE SET NULL
) ENGINE=InnoDB;


