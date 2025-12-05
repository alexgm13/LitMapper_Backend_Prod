-- name: existing_doi(doi)$
-- Devuelve true si el DOI existe, false si no. El '$' indica que devuelve un solo valor escalar.
SELECT EXISTS(SELECT 1 FROM articulo WHERE doi = :doi);

-- name: get_articule_doi(doi)^
-- Busca si existe el artículo. Si existe, devuelve los campos solicitados.
SELECT id_articulo, doi, titulo, resumen 
FROM articulo 
WHERE doi = :doi;


-- name: create_articulo(doi, titulo, resumen)^
-- Inserta el artículo y devuelve los datos generados (especialmente el ID).
INSERT INTO articulo (
    doi, 
    titulo, 
    resumen
) 
VALUES (
    :doi, 
    :titulo, 
    :resumen
)
RETURNING id_articulo, doi, titulo, resumen;

-- name: upsert_articulo_detalle(id_proyecto, id_articulo, es_relevante, justificacion)^
-- Inserta un detalle. Si ya existe la combinación proyecto-articulo, actualiza los datos.
INSERT INTO articulo_detalle (
    id_proyecto, 
    id_articulo, 
    es_relevante, 
    justificacion
)
VALUES (
    :id_proyecto, 
    :id_articulo, 
    :es_relevante, 
    :justificacion
)
ON CONFLICT (id_proyecto, id_articulo) 
DO UPDATE SET 
    es_relevante = EXCLUDED.es_relevante,
    justificacion = EXCLUDED.justificacion,
    fecha_modificacion = CURRENT_TIMESTAMP
RETURNING id_articulo_detalle, id_proyecto, id_articulo;