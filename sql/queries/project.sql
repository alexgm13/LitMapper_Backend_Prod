-- name: list_by_user
-- fn: Obtiene todos los proyectos de un usuario ordenados por fecha (del más nuevo al más viejo)
SELECT 
    id_proyecto, 
    titulo, 
    descripcion, 
    fase, 
    estado, 
    fecha_creacion, 
    fecha_modificacion
FROM proyecto
WHERE id_usuario = :id_usuario
ORDER BY fecha_creacion DESC;

-- name: create-project<!
-- fn: Crea un nuevo proyecto y devuelve los datos básicos
INSERT INTO proyecto (titulo, descripcion, id_usuario)
VALUES (:titulo, :descripcion, :id_usuario)
RETURNING id_proyecto, titulo, fase, estado, fecha_creacion;