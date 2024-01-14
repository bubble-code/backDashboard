--select fk.name as foreingn_key_name
--from sys.foreign_keys as fk
--inner join
--sys.tables as tp on fk.parent_object_id = tp.object_id

--where tp.name = 'tbMaestroCargo'

SELECT 
    view_name = o.name,
    definition
FROM 
    sys.sql_modules m
INNER JOIN 
    sys.objects o ON m.object_id = o.object_id
WHERE 
    definition LIKE '%tbMaestroCargo%'
    AND o.type_desc = 'VIEW';
