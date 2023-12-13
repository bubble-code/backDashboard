from sqlalchemy import create_engine, MetaData
from sqlalchemy_schemadisplay import create_schema_graph

# Conexión a la base de datos
server = 'srvsql'
database = 'SolmicroERP6_PruebasSub'
username = 'sa'
password = 'Altai2021'
driver = 'ODBC+Driver+17+for+SQL+Server'

connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

# Cargar la tabla que deseas mapear
table_name = 'tbOfertaComercialCabecera'
metadata = MetaData()
table = metadata.reflect(bind=engine, only=[table_name])

# Generar el mapeo en un archivo Python
with open('tbOfertaComercialCabecera.py', 'w') as file:
    file.write(f"from sqlalchemy import Table, Column, Integer, ...\n\n")
    file.write("metadata = MetaData()\n\n")
    for t in table.values():
        file.write(f"{t.name} = Table('{t.name}', metadata, autoload=True, autoload_with=engine)\n")