DECLARE @generatedQuery NVARCHAR(MAX);

-- Especifica las tablas de origen y destino
--DECLARE @tablaOrigen NVARCHAR(128) = 'tbMaestroCentro';
--DECLARE @tablaDestino NVARCHAR(128) = 'SolmicroERP6_Favram.dbo.tbMaestroCentro';

-- Llama a la función para generar el query
 --exec ALE_GenerarQueryUpdate(N'tbMaestroCentro',N'SolmicroERP6_Favram.dbo.tbMaestroCentro');
-- Imprime o ejecuta el query generado
--PRINT @generatedQuery;
--EXEC sp_executesql @generatedQuery; -- Descomenta esta línea si deseas ejecutar el query directamente

declare @t Table(nameT nvarchar(200))
declare @tablaOrigen NVARCHAR(128) = 'tbMaestroCentro', @tablaDestino NVARCHAR(128) = 'tbMaestroCentro', @query nvarchar(500) = 'UPDATE '+ 'tbMaestroCentro' +' SET '
declare @query2 nvarchar(500) = 'inner join '+ 'tbMaestroCentro' + ' on '

 insert into @t(nameT) (SELECT concat(QUOTENAME(COLUMN_NAME),'= ',@tablaOrigen ,'.'+QUOTENAME(COLUMN_NAME)) 
 FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = @tablaDestino)

 select CONCAT(@query, ( select STRING_AGG(nameT,',') from @t))

--DECLARE @ColumnNames NVARCHAR(MAX);

--SELECT @ColumnNames = STRING_AGG(QUOTENAME(COLUMN_NAME), ', ')
--FROM INFORMATION_SCHEMA.COLUMNS
--WHERE TABLE_NAME = 'tbMaestroCentro'


--PRINT 'UPDATE tbMaestroCentro SET ' + @ColumnNames;
