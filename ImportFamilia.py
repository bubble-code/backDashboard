from sqlalchemy import create_engine,text, Integer, select
from Conexion import MainConexion
from models.MaestroFamilia import MaestroFamilia
from CExcel import CExcel
from sqlalchemy.orm import sessionmaker
import pandas as pd


class ManagerFamilia:
    def __init__(self):
        self.ruta = r'Familas.xlsx'

    def get_Familia_Industry(self):
        conexion = MainConexion()
        try:
            conn = conexion.Open_Conn_Industry()
            if conn:
                print("Get Datos desde industry...")   
                query = text(
                    f"SELECT Codigo, Descripcion, FechaDeAlta, FechaUltimaModificacion, UsuarioAlta, UsuarioModificacion, PorcentajeComision, MesesGarantia, CuentaCompra, CuentaVenta, CuentaStock, SubcuentaCompra, SubcuentaVenta,SubcuentaStock, SistemaDistribucionObjetivos, Altai_Control, VisibleECommerce FROM MFamilia") 
                result = conn.execute(query).fetchall()
                print("Completed")
                return result    
        except Exception as e:
            print('Error en la conexion: ',e)
        finally:
            if conn:
                conn.Close()

    def serializar(self, data):
        result = []
        print("Serializando")
        for row in data:
            result.append(MaestroFamilia(row))
        print("Finished")
        return result


impFamilia = ManagerFamilia()
