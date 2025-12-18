CREATE TABLE IF NOT EXISTS tareas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    completado BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_tarea_usuario 
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id) 
        ON DELETE CASCADE
) ENGINE=InnoDB;