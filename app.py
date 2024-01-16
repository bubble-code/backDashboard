from flask import Flask, jsonify, request
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
from models.Models import db, OrdenFabricacion, MaestroArticulo
from InfoTables import SQLTableInfo


def create_app():
    app = Flask(__name__)
    CORS(app)
    server_industry = r'SERVIDOR'
    server_solmicro = r'srvsql'
    database_solmicro = 'SolmicroERP6_PruebasSub'
    username_solmicro = 'sa'
    password_solmicro = 'Altai2021'
    # Configuración de SQLAlchemy para la conexión a SQL Server
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{username_solmicro}:{password_solmicro}@{server_solmicro}/{database_solmicro}?driver=ODBC+Driver+17+for+SQL+Server'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/api/of', methods=['GET'])
    def obtener_ordenes_fabricacion():
        search_term = request.args.get('term', '')
        if len(search_term) < 2:
            return jsonify([])
        ordenes = OrdenFabricacion.query.filter(OrdenFabricacion.NOrden.contains(
            search_term)).with_entities(OrdenFabricacion.NOrden).all()
        ordenes = [orden[0] for orden in ordenes]
        return jsonify(ordenes)

    # Endpoint para obtener detalles de una orden de fabricación por su ID
    @app.route('/api/orden/<string:orden_no>')
    def obtener_detalle_orden(orden_no):
        orden = OrdenFabricacion.query.filter_by(NOrden=orden_no).first()
        # detalles_orden = [ordenF.serialize() for ordenF in orden if ordenF]
        if orden:
            return jsonify(orden.serialize())
        else:
            return jsonify({'mensaje': 'Orden no encontrada'}), 404

    @app.route('/api/articulos', methods=['GET'])
    def obtener_articulos():
        id_articulo = request.args.get('IDArticulo')
        if id_articulo:
            articulo = MaestroArticulo.query.filter_by(
                IDArticulo=id_articulo).first()
            if articulo:
                return jsonify(articulo.serialize())
            else:
                return jsonify({'mensaje': 'Artículo no encontrado'}), 404
        else:
            articulos = MaestroArticulo.query.all()
            articulos_serializados = [articulo.serialize() for articulo in articulos]
            return articulos_serializados
        
    @app.route('/api/obtener_tablas_maestro',methods=['GET'])
    def get_maestros_name_tables():
        get_tables = SQLTableInfo()
        tables = get_tables.get_tables_with_keyword()
        return jsonify(tables)
    
    @app.route('/api/maestro/<string:name_table>')
    def get_maestros_name_data(name_table):
        manager_table = SQLTableInfo()
        dataTable = manager_table.get_data(nameTable=name_table)
        return jsonify(dataTable)
    
    @app.route('/api/maestroNew/<string:name_table>')
    def get_maestros_name_data_new(name_table):
        manager_table = SQLTableInfo()
        dataTable = manager_table.get_data_new(nameTable=name_table)
        return jsonify(dataTable)
    
    @app.route('/api/maestroUpdate/<string:name_table>')
    def get_maestros_update(name_table):
        manager_table = SQLTableInfo()
        manager_table.ipdate_into_aleNameTablas(name_table)
        


    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
