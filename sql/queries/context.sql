-- name: insert_context(id_proyecto, area_general, tema_especifico, problema_investigacion, metodologia)$
INSERT INTO contexto (id_proyecto, area_general, tema_especifico, problema_investigacion, metodologia)
VALUES (:id_proyecto, :area_general, :tema_especifico, :problema_investigacion, :metodologia)
ON CONFLICT (id_proyecto) 
DO UPDATE SET 
    area_general = EXCLUDED.area_general,
    tema_especifico = EXCLUDED.tema_especifico,
    problema_investigacion = EXCLUDED.problema_investigacion,
    metodologia = EXCLUDED.metodologia,
    fecha_modificacion = CURRENT_TIMESTAMP
RETURNING id_contexto;

-- name: get_context(id_proyecto)^
SELECT 
    id_contexto,
    id_proyecto,
    area_general,
    tema_especifico,
    problema_investigacion,
    metodologia
FROM contexto WHERE id_proyecto = :id_proyecto;