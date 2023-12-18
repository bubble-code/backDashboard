from sqlalchemy import create_engine, text, bindparam, Integer, select, func
from Conexion import MainConexion
from sqlalchemy.orm import sessionmaker
import pandas as pd

class Estructura:
    def __init__(self):
        self.ruta_archivo = r'ArtFormateados2.xlsx' 
        self.hoja_excel = 'Sheet1'

    def getDatosEstructIndustry(self):
        mainConexion = MainConexion()
        try:
            conn = mainConexion.Open_Conn_Industry()
            if conn:
                print("Get DatosArtIndustry")
                query = text(
                    f"SELECT Padre, Hijo, PosicionPlano, UnidadesBrutas, UnidadesNetas, PerdidaPreparacion, FechaInicioIngenieria, FechaFinalIngenieria, FabricacionPorLotes, FechaDeAlta, FechaUltimaModificacion, UsuarioAlta, UsuarioModificacion, Version, GuardaVersion, Secuencia, NoGenerar, FaseConsumo, FormulaBrutas, FormulaNetas, PriorizarReservas FROM MConjunto")
                result = conn.execute(query).fetchall()
                grouped_result = {}
                for row in result:
                    padre = row['Padre']
                    if padre not in grouped_result:
                        grouped_result[padre] = []
                    grouped_result[padre].append(row)
                print("Completed")
                return grouped_result
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()

    def CheckArticuloSolmicro(self,listArticulos):
        mainConexion = MainConexion()
        noPresent = []
        sinEstructura = []
        try:
            conn = mainConexion.Open_Conn_Solmicro()
            if conn:
                print("Check articulo in Solmicro")
                for articulo in listArticulos:
                    print(articulo[0])
                    query = text(f"SELECT top(1) IDArticulo FROM tbMaestroArticulo WHERE IDArticulo = N'{articulo[0]}'")
                    result = conn.execute(query).fetchone()
                    if result:
                        query2 = text(f"SELECT top(1) IDArticulo FROM  tbEstructura where IDArticulo = N'{articulo[0]}'")
                        result2 = conn.execute(query2).fetchone()
                        if result2:
                            sinEstructura.append(articulo)
                    else:
                        noPresent.append(articulo)
                conn.commit()
                conn.close()
                print("Completado")
            return sinEstructura
        except Exception as e:
            print("Error en la consulta:", e)
            return sinEstructura