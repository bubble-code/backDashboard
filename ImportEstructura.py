from sqlalchemy import create_engine, text, bindparam, Integer, select, func
from Conexion import MainConexion
from ImportArticuloAlmacen import MaestroArticuloAlmacenManager
from models.Estructura import TbEstructura
from CExcel import CExcel
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
                print("Completado")
                return result
                # grouped_result = {}
                # for row in result:
                #     padre = row['Padre']
                #     if padre not in grouped_result:
                #         grouped_result[padre] = []
                #     grouped_result[padre].append(row)
                # print("Completed")
                # return grouped_result
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()

    def serializar(self, data):
        result = []
        print("Serializando")
        for row in data:
            result.append(
                {
                    "IDEstrComp": None,
                    "IDTipoEstructura": None,
                    "IDArticulo": row[0],
                    "IDEstructura": f'01',
                    "IDComponente": row[1],
                    "Cantidad": f'{row[3]}',
                    "Merma": 0.00000000,
                    "Secuencia": row[17],
                    "FechaCreacionAudi": None,
                    "FechaModificacionAudi": None,
                    "UsuarioAudi": None,
                    "IDUdMedidaProduccion": None,
                    "Factor": 1.00000000,
                    "CantidadProduccion": f'{row[3]}',
                    "UsuarioCreacionAudi": None
                }
            )
        print("End Serializer")
        return result

    def chunks(self, list, n):
        for i in range(0, len(list), n):
            yeild = list[i:i+n]

    def checkImportacion(self):
        excel = CExcel()
        list_IDEstrComp = excel.CargarExcel(
            ruta_archivo=f"ImportEstructura2.xlsx", hoja_excel="Sheet1", columnas=["IDEstrComp","IDArticulo","IDComponente"])
        print(len(list_IDEstrComp["IDEstrComp"]))
        resultados = []
        mainconexion = MainConexion()
        try:
            conn = mainconexion.Open_Conn_Solmicro()
            if conn:
                print("Starting")
                query = text(f"SELECT IDEstrComp FROM tbEstructura")
                result = conn.execute(query).fetchall()
                result_list = [item[0] for item in result]
                for idx,row in list_IDEstrComp.iterrows():
                    if row["IDEstrComp"] not in result_list:
                        resultados.append(row)
                conn.close()
                print("Check completado")
                return resultados
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()

    def checkMaestroArticulosAlmacen(self):
        elementos_no_encontrados = []
        manager_art_almacen = MaestroArticuloAlmacenManager()
        print("instacia manager")
        tbEstructu = TbEstructura()
        print("instacia estructura")
        id_componente_data = list(set(tbEstructu.get_column_data("IDComponente")))
        print("lista de componentes",len(id_componente_data))
        for component in id_componente_data:
            print(component,len(elementos_no_encontrados))
            result = manager_art_almacen.filter_by_id(id=component)
            if not result:
                elementos_no_encontrados.append(component)
        print(len(elementos_no_encontrados))
        print("Elementos no encontrados")
        data_from_industry = manager_art_almacen.get_data_from_industry(elementos_no_encontrados)
        print("Data from industry", len(data_from_industry))
        serialized_data = manager_art_almacen.serializar(data_from_industry)
        print("Serialized data", len(serialized_data))
        manager_art_almacen.export_to_excel(name="ArticulosAlmacen.xlsx",data=serialized_data)
    

    @staticmethod
    def export_to_excel_art_desd_indus(data):
        print("Exporting")
        df = pd.DataFrame(data, columns=['IDEstrComp', 'IDTipoEstructura', 'IDArticulo', 'IDEstructura', 'IDComponente', 'Cantidad', 'Merma', 'Secuencia',
                        'FechaCreacionAudi', 'FechaModificacionAudi', 'UsuarioAudi', 'IDUdMedidaProduccion', 'Factor', 'CantidadProduccion', 'UsuarioCreacionAudi'])
        df.to_excel("ImportRuta.xlsx", index=False)
        print("End Exportacion")

    @staticmethod
    def export_to_excel_missing(data):
        print("Exporting")
        df = pd.DataFrame(data,columns=["IDEstrComp", "IDArticulo", "IDComponente"])
        df.to_excel("MissingStructure.xlsx", index=False)
        print("End Exportacion")


obj = Estructura()
input("Continue")
# datos_industry = obj.getDatosEstructIndustry()
# print(len(datos_industry))
# input("Continue")
# serialized_datos = obj.serializar(data=datos_industry)
# obj.export_to_excel_art_desd_indus(data=serialized_datos)
# input("Continue")
# result = obj.checkMaestroArticulosAlmacen()
result = obj.checkImportacion()
input("Continue")
print(len(result))
print("****************************************************************")
# print(result)
input("continue")
obj.export_to_excel_missing(data=result)

