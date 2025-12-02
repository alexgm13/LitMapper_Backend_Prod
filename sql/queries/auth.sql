-- name: create-user<!
-- fn: Crea el usuario y retorna su ID para usarlo despues
INSERT INTO usuario (email, contrasena, id_rol) 
VALUES (:email, :contrasena, :id_rol)
RETURNING id_usuario, email, id_rol, estado;

-- name: create-profile<!
-- fn: Crea el perfil asociado al usuario recien creado
INSERT INTO perfil (nombre, fecha_nacimiento, genero, id_usuario)
VALUES (:nombre, :fecha_nacimiento, :genero, :id_usuario)
RETURNING id_perfil, nombre, fecha_nacimiento, genero;

-- name: get-user-login-data^
SELECT u.id_usuario, u.email, u.contrasena, u.id_rol, u.estado, p.nombre
FROM usuario u
INNER JOIN perfil p ON p.id_usuario = u.id_usuario
WHERE u.email = :email;