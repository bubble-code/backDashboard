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

    @staticmethod
    def export_to_excel_art_desd_indus(data):
        print("Exporting")
        df = pd.DataFrame(data, columns=['IDEstrComp', 'IDTipoEstructura', 'IDArticulo', 'IDEstructura', 'IDComponente', 'Cantidad', 'Merma', 'Secuencia','FechaCreacionAudi', 'FechaModificacionAudi', 'UsuarioAudi','IDUdMedidaProduccion','Factor', 'CantidadProduccion', 'UsuarioCreacionAudi'])
        df.to_excel("ImportRuta.xlsx", index=False)
        print("End Exportacion")

    # def CheckArticuloSolmicro(self, listArticulos):
    #     mainConexion = MainConexion()
    #     result = {
    #         "noPresent": [],
    #         "sinEstructura": []
    #     }

    #     try:
    #         conn = mainConexion.Open_Conn_Solmicro()
    #         if conn:
    #             print("Check articulo in Solmicro")
    #             for articulo in listArticulos:
    #                 print(articulo)
    #                 query = text(
    #                     f"SELECT top(1) IDArticulo FROM tbMaestroArticulo WHERE IDArticulo = N'{articulo}'")
    #                 result = conn.execute(query).fetchone()
    #                 if result:
    #                     query2 = text(
    #                         f"SELECT IDEstrComp, IDTipoEstructura, IDArticulo, IDEstructura, IDComponente, Cantidad, Merma, Secuencia, FechaCreacionAudi, FechaModificacionAudi, UsuarioAudi, IDUdMedidaProduccion, Factor, CantidadProduccion,UsuarioCreacionAudi FROM tbEstructura WHERE IDArticulo = N'{articulo}' and (IDEstructura = N'01')")
    #                     result2 = conn.execute(query2).fetchone()
    #                     if not result2:
    #                         result["sinEstructura"].append(articulo)
    #                     else:
    #                         for hijo in listArticulos[articulo]:

    #                 else:
    #                     noPresent.append(articulo)
    #             conn.commit()
    #             conn.close()
    #             print("Completado")
    #         return sinEstructura
    #     except Exception as e:
    #         print("Error en la consulta:", e)
    #         return sinEstructura


obj = Estructura()
input("Continue")
datos_industry = obj.getDatosEstructIndustry()
print(len(datos_industry))
input("Continue")
serialized_datos = obj.serializar(data=datos_industry)
obj.export_to_excel_art_desd_indus(data=serialized_datos)
input("Continue")