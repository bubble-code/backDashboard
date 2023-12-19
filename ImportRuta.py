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
        try:
            conn = mainConexion.Open_Conn_Industry()
            if conn:
                print("Get DatosArtIndustry")
                query = text(
                    f"SELECT Articulo, Fase, Descripcion, TipoFase, Centro, Ritmo, OperariosOperacion, OperariosPreparacion, TiempoPreparacion, TipoUtillaje, CodigoPreparacion, LoteMinimo, LoteLiberacion, FechaDeAlta,FechaUltimaModificacion, UsuarioAlta, UsuarioModificacion, Autocontrol, Version, GuardaVersion, UnidadesPorCiclo, TiempoCiclo, UnidadTiempoCiclo, IDDocumAdjuntos, TiempoHorasPieza, UnidadHorasPieza,CodigoMixProduction, Paralelo, RitmoCrono FROM MFase")
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
    
    def serializar(self,datos):
        result =[]
        print("Serializando datos")
        for row in datos:
            result.append({
                "IDRutaOp": None,
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
                "IDTipoRuta": None,
                "TiempoPrep": 0.00000000,
                "UdTiempoPrep":1,
                "TiempoEjecUnit": row[24] ,
                "UdTiempoEjec":1,
                "FechaCreacionAudi": None,
                "FechaModificacionAudi": None,
                "UsuarioAudi": None,
                "TiempoCiclo":0.00000000,
                "UdTiempoCiclo":1,
                "LoteCiclo":0.00000000,
                "PlazoSub": 0,
                "UdTiempoPlazo":1,
                "SolapePor": 0.00000000,
                "Ciclo": 0,
                "Rendimiento": 100.00000000,
                "IDCContable": None,
                "IdDocumentoEspecificacion": None,
                "CantidadTiempo100": 0.00000000,
                "SolapeLote": 0.00000000,
                "OcupacionMaquina":0.00000000,
                "Texto":None,
                "UsuarioCreacionAudi": None,
                "TiempoProgramacion": row[12]
            })
        print("End Serializado")
        return result
    
    @staticmethod
    def export_to_excel_art_desd_indus(data):
        print("Exporting")
        df = pd.DataFrame(data, columns=['IDRutaOp',	'IDArticulo',	'IDRuta',	'Secuencia',	'TipoOperacion',	'IDOperacion',	'DescOperacion',	'Critica',	'IDCentro',	'FactorHombre',	'IDUdProduccion',	'CantidadTiempo',	'UdTiempo',	'FactorProduccion',	'ControlProduccion',	'IDTipoRuta',	'TiempoPrep',	'UdTiempoPrep',	'TiempoEjecUnit',	'UdTiempoEjec',	'FechaCreacionAudi',	'FechaModificacionAudi',	'UsuarioAudi',	'TiempoCiclo',	'UdTiempoCiclo',	'LoteCiclo',	'PlazoSub',	'UdTiempoPlazo',	'SolapePor',	'Ciclo',	'Rendimiento',	'IDCContable',	'IdDocumentoEspecificacion',	'CantidadTiempo100',	'SolapeLote',	'OcupacionMaquina',	'Texto',	'UsuarioCreacionAudi',	'TiempoProgramacion'])
        df.to_excel("ImportRuta.xlsx", index=False)
        print("End Exportacion")

obj = Ruta()
input("Creado obj")
datos_industry = obj.getDatosRutaIndustry()
print(len(datos_industry))
input("continue")
serielized_datos = obj.serializar(datos=datos_industry)
input("continue")
obj.export_to_excel_art_desd_indus(data=serielized_datos)
input("continue")
