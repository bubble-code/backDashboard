from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

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

# Inicialización de SQLAlchemy
db = SQLAlchemy(app)


class OrdenFabricacion(db.Model):
    __tablename__ = 'tbOrdenFabricacion'

    id = db.Column(db.Integer, primary_key=True)
    NOrden = db.Column(db.String(25))


# Ruta para obtener los datos para el Autocomplete
@app.route('/api/of')
def obtener_ordenes_fabricacion():
    ordenes = OrdenFabricacion.query.with_entities(OrdenFabricacion.NOrden).all()
    ordenes = [orden[0] for orden in ordenes]
    return jsonify(ordenes)

if __name__ == '__main__':
    app.run(debug=True)
