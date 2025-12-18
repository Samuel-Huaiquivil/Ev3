CREATE TABLE IF NOT EXISTS direcciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT UNIQUE, 
    calle VARCHAR(255),
    departamento VARCHAR(100),
    ciudad VARCHAR(100),
    codigo_postal VARCHAR(50),
    lat VARCHAR(50),
    lng VARCHAR(50),
    CONSTRAINT fk_direccion_usuario 
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id) 
        ON DELETE CASCADE
) ENGINE=InnoDB;
