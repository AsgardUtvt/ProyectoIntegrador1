
CREATE TABLE Sub_Consultorio
(
id_sub_consultorio INT AUTO_INCREMENT PRIMARY KEY,
sub_consultorio_name VARCHAR(50) NOT NULL UNIQUE,
sub_consultorio_calle VARCHAR(100),
sub_consultorio_colonia VARCHAR(100),
sub_consultorio_num_exterior VARCHAR(3),
sub_consultorio_num_interior VARCHAR(3),
sub_consultorio_localidad VARCHAR(100),
sub_consultorio_telefono VARCHAR(13),
sub_consultorio_telefono_dos VARCHAR(13),
sub_id_estado INT NOT NULL,
id_consultorio INT NOT NULL
);

SET FOREIGN_KEY_CHECKS = 0;
ALTER TABLE Sub_Consultorio
    DROP FOREIGN KEY IF EXISTS FK_SUB_CONSULTORIO_CONSULTORIO;
ALTER TABLE Sub_Consultorio
    ADD CONSTRAINT FK_SUB_CONSULTORIO_CONSULTORIO 
    FOREIGN KEY (id_consultorio)
    REFERENCES Consultorio(id_consultorio)
    ON DELETE CASCADE
    ON UPDATE CASCADE;
SET FOREIGN_KEY_CHECKS = 1;
