from sqlalchemy import create_engine, text, bindparam, Integer, select, func
from Conexion import MainConexion
from sqlalchemy.orm import sessionmaker
import pandas as pd


class Ruta:
    def __init__(self):
        self.ruta_archivo = r'ArtFormateados2.xlsx'
        self.hoja_excel = 'Sheet1'
    
    def getDatosRutaIndustry(self):
        mainConexion = MainConexion()
        grouped_result = {}
        try:
            conn = mainConexion.Open_Conn_Industry()
            if conn:
                print("Get DatosArtIndustry")
                query = text(
                    f"SELECT Articulo, Fase, Descripcion, TipoFase, Centro, Ritmo, OperariosOperacion, OperariosPreparacion, TiempoPreparacion, TipoUtillaje, CodigoPreparacion, LoteMinimo, LoteLiberacion, FechaDeAlta,FechaUltimaModificacion, UsuarioAlta, UsuarioModificacion, Autocontrol, Version, GuardaVersion, UnidadesPorCiclo, TiempoCiclo, UnidadTiempoCiclo, IDDocumAdjuntos, TiempoHorasPieza, UnidadHorasPieza,CodigoMixProduction, Paralelo, RitmoCrono FROM MFase where Articulo = N'S01.03.000'")
                result = conn.execute(query).fetchall()
                print("Completado")
                return result                
                # for row in result:
                #     articulo = row[0]
                #     if articulo not in grouped_result:
                #         grouped_result[articulo] = []
                #     grouped_result[articulo].append(row)
                # print("Completed")
                # return grouped_result
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()

    def checkRuta(self,data):
        mainConexion = MainConexion()
        fases = []
        try:
            conn = mainConexion.Open_Conn_Solmicro()
            if conn:
                for articulo in data:
                    print(articulo)
                    query = text(f"SELECT IDRutaOp, IDArticulo, IDRuta, Secuencia, TipoOperacion, IDOperacion, DescOperacion, Critica, IDCentro, FactorHombre, IDUdProduccion, CantidadTiempo, UdTiempo, FactorProduccion, ControlProduccion, IDTipoRuta, TiempoPrep, UdTiempoPrep, TiempoEjecUnit, UdTiempoEjec, FechaCreacionAudi, FechaModificacionAudi, UsuarioAudi, TiempoCiclo, UdTiempoCiclo, LoteCiclo, PlazoSub, UdTiempoPlazo, SolapePor, Ciclo, Rendimiento, IDCContable, IdDocumentoEspecificacion, CantidadTiempo100, SolapeLote, OcupacionMaquina, Texto, UsuarioCreacionAudi, TiempoProgramacion FROM tbRuta where IDArticulo= N'{articulo}'")
                    result = conn.execute(query).fetchall()
                    if len(data[articulo])> len(result):
                        for fase in data[articulo]:
                            if fase["Fase"] != result["Secuencia"] and fase["Centro"]!=result["IDCentro"]:
                                fases.append(fase)
                return fases
        except Exception as e:
            print("Error en la consulta:",e)
        finally:
            if conn:
                conn.close()
    
    def serializar(self,datos):
        result =[]
        print("Serializando datos")
        for row in datos:
            result.append({
                "IDRutaOp": 'NULL',
                "IDArticulo": row[0],
                "IDRuta": '01',
                "Secuencia":row[1],
                "TipoOperacion":0, 
                "IDOperacion": row[1],
                "DescOperacion": row[2],
                "Critica": 0,
                "IDCentro": row[4],
                "FactorHombre": row[6],
                "IDUdProduccion":'u.',
                "CantidadTiempo": row[5],
                "UdTiempo": 1,
                "FactorProduccion": 1,
                "ControlProduccion": 1,
                "IDTipoRuta": 'NULL',
                "TiempoPrep": 0.00000000,
                "UdTiempoPrep":1,
                "TiempoEjecUnit": row[24] ,
                "UdTiempoEjec":1,
                "FechaCreacionAudi": 'NULL',
                "FechaModificacionAudi": 'NULL',
                "UsuarioAudi": 'NULL',
                "TiempoCiclo":0.00000000,
                "UdTiempoCiclo":1,
                "LoteCiclo":0.00000000,
                "PlazoSub": 0,
                "UdTiempoPlazo":1,
                "SolapePor": 0.00000000,
                "Ciclo": 0,
                "Rendimiento": 100.00000000,
                "IDCContable": 'NULL',
                "IdDocumentoEspecificacion": 'NULL',
                "CantidadTiempo100": 0.00000000,
                "SolapeLote": 0.00000000,
                "OcupacionMaquina":0.00000000,
                "Texto":'NULL',
                "UsuarioCreacionAudi": 'NULL',
                "TiempoProgramacion": row[12]
            })
        print("End Serializado")
        return result
    
    @staticmethod
    def export_to_excel_art_desd_indus(data):
        print("Exporting")
        df = pd.DataFrame(data, columns=['IDRutaOp','IDArticulo',	'IDRuta',	'Secuencia','TipoOperacion','IDOperacion','DescOperacion','Critica','IDCentro','FactorHombre','IDUdProduccion','CantidadTiempo','UdTiempo','FactorProduccion','ControlProduccion','IDTipoRuta','TiempoPrep','UdTiempoPrep','TiempoEjecUnit','UdTiempoEjec','FechaCreacionAudi','FechaModificacionAudi','UsuarioAudi','TiempoCiclo','UdTiempoCiclo','LoteCiclo','PlazoSub','UdTiempoPlazo','SolapePor','Ciclo','Rendimiento','IDCContable','IdDocumentoEspecificacion','CantidadTiempo100','SolapeLote','OcupacionMaquina','Texto','UsuarioCreacionAudi','TiempoProgramacion'])
        df.to_excel("ExportRutaS01.03.000.xlsx", index=False)
        print("End Exportacion")

obj = Ruta()
input("Creado obj")
datos_industry = obj.getDatosRutaIndustry()
print(datos_industry)
input("continue")
# missingFases =  obj.checkRuta(data=datos_industry)
# print(len(missingFases))
serielized_datos = obj.serializar(datos=datos_industry)
print(serielized_datos[:10])
input("continue")
obj.export_to_excel_art_desd_indus(data=serielized_datos)
input("continue")
