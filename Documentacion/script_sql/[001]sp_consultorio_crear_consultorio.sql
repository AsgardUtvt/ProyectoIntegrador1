-- DESC Consultorio;
-- En caso de existir elimina el estore procedu.
DROP PROCEDURE IF EXISTS sp_crear_consultorio;

DELIMITER $$
CREATE PROCEDURE sp_crear_consultorio(c_name VARCHAR(50), c_calle VARCHAR(100), c_colonia VARCHAR(100), c_num_exterior VARCHAR(3), c_num_interior VARCHAR(3), c_estado INT, c_localida VARCHAR(100), c_telefono VARCHAR(13), c_telefono_dos VARCHAR(13), c_municipio VARCHAR(100), OUT c_id INT)
BEGIN
    -- Se genera un insret de a la tabla consultorio
    INSERT INTO Consultorio(consultorio_name, consultorio_calle, consultorio_colonia, consultorio_num_exterior, consultorio_num_interior, consultorio_localidad, id_estado, consultorio_telefono, consultorio_telefono_dos, consultorio_municipio)
    VALUES(c_name, c_calle, c_colonia, c_num_exterior, c_num_interior, c_localida, c_estado, c_telefono, c_telefono_dos, c_municipio);
    -- Se obtiene el útlimo id del instert y se retorna
    SET c_id = LAST_INSERT_ID();
END$$
DELIMITER ;
