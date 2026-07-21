DROP PROCEDURE IF EXISTS sp_usuario_crear_usuario;
/*
DESC Usuario;
*/
DELIMITER $$

CREATE PROCEDURE sp_usuario_crear_usuario(IN u_name VARCHAR(50),IN u_paterno VARCHAR(50),IN u_materno VARCHAR(50),IN u_password VARCHAR(100),IN u_cedula_profesional VARCHAR(13),IN u_cedula_especialidad VARCHAR(13),IN u_tipo_usuario INT,IN u_consultorio INT,IN u_escuela INT, OUT u_id INT)
BEGIN
    INSERT INTO Usuario(usuario_name, usuario_paterno, usuario_materno, usuario_password, usuario_cedula_profesional, usuario_cedula_especialidad, id_tipo_usuario, id_consultorio, id_escuela)
    VALUES(u_name, u_paterno, u_materno, u_password, u_cedula_profesional, u_cedula_especialidad, u_tipo_usuario, u_consultorio, u_escuela);
    SET u_id = LAST_INSERT_ID();
END$$
DELIMITER ;
