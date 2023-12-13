from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.ext.automap import automap_base
import subprocess

db = SQLAlchemy()

db_connection_config = {
    'server': 'SERVIDOR',
    'solmicro_server': 'srvsql',
    'database': 'SolmicroERP6_PruebasSub',
    'username': 'sa',
    'password': 'Altai2021',
    'driver': 'ODBC+Driver+17+for+SQL+Server'
}

def get_db_uri():
    return f"mssql+pyodbc://{db_connection_config['username']}:{db_connection_config['password']}@{db_connection_config['solmicro_server']}/{db_connection_config['database']}?driver={db_connection_config['driver']}"

# def automap_tables():
#     db_uri = get_db_uri()
#     db.app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#     db.init_app(app)
#     from models.ordenFabricacion import OrdenFabricacion
#     db.Model.metadata.reflect(db.engine)
#     Base = automap_base(metadata= db.Model.metadata)
#     Base.prepare()

#     OrdenFabricacion = Base.classes.tbOrdenFabricacion

#     return {
#         'OrdenFabricacion': OrdenFabricacion
#     }

def generate_models_file():
    command = f"sqlacodegen_v2 --generator dataclasses --outfile models.py {get_db_uri()}"
    subprocess.run(command, shell=True)

generate_models_file()