from sqlalchemy import create_engine, text, bindparam, Integer, select
from sqlalchemy.orm import sessionmaker
import pandas as pd


class GetSubfamilias:
    def __init__(self):
        self.server_industry = r'SERVIDOR'
        self.server_solmicro = r'srvsql'
        self.database_solmicro = 'SolmicroERP6_PruebasSub'
        self.database_industry = 'IPFavram'
        self.username_solmicro = 'sa'
        self.password_solmicro = 'Altai2021'
        self.password_industry = '71zl6p9h'
        self.connection_string_solmicro = create_engine(
            f'mssql+pyodbc://{self.username_solmicro}:{self.password_solmicro}@{self.server_solmicro}/{self.database_solmicro}?driver=SQL+Server')
        self.connection_string_industry = create_engine(
            f'mssql+pyodbc://{self.username_solmicro}:{self.password_industry}@{self.server_industry}/{self.database_industry}?driver=SQL+Server')
        self.connection = None
        self.connection_industry = None
        self.tables_info = []
        self.connection_solmicro = f'DRIVER={{SQL Server}};SERVER={self.server_solmicro};DATABASE={self.database_solmicro};UID={self.username_solmicro};PWD={self.password_solmicro}'
        self.ruta_archivo = r'ArtFormateados2.xlsx'
        self.hoja_excel = 'Sheet1'

    def Open_Conn_Solmicro(self):
        try:
            self.connection = self.connection_string_solmicro.connect()
            return self.connection
        except Exception as e:
            print("Error opening connection: ", e)

    def Open_Conn_Industry(self):
        try:
            self.connection = self.connection_string_industry.connect()
            return self.connection
        except Exception as e:
            print("Error opening connection: ", e)

    def get_subfamiliIndustry(self, tipo=1):
        try:
            conn = self.Open_Conn_Industry()
            if conn:
                print("Get sub familia from Industry")
                query = text(
                    f"SELECT DISTINCT MFamilia.Codigo, MFamilia.Descripcion, MArticulo.TipoArticulo FROM MFamilia INNER JOIN MArticulo ON MFamilia.Codigo = MArticulo.Familia WHERE (MArticulo.TipoArticulo = N'{tipo}') GROUP BY MFamilia.Codigo, MFamilia.Descripcion")
                result = conn.execute(query).fetchall()
                print("Completed")
                return result
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()

    def checkSubFamiliaSolmicro(self,listSubfamilia):
        resultados = []
        try:
            conn = self.Open_Conn_Solmicro()
            if conn:
                print("Check subFamilia in Solmicro")
                for IDSubfamilia, descrip in listSubfamilia:
                    query = text(f"SELECT top(1) IDSubfamilia FROM tbMaestroSubfamilia WHERE IDFamilia = 'VENTACLIEN'  and IDSubfamilia = N'{IDSubfamilia}' ")
                    result = conn.execute(query).fetchone()
                    if not result:
                        resultados.append(IDSubfamilia)
                conn.commit()
                conn.close()
                print("Completado")
            return resultados
        except Exception as e:
            print("Error en la consulta:", e)
            return resultados
    
    def serializer(self,data):
        result =[]
        print("Serializando datos")
        for row in data:
            result.append({

            })
        
    @staticmethod
    def export_subFamilias_excel(subFamiliasList):
        print("Exporting")
        df = pd.DataFrame(subFamiliasList,columns=["SubFamilias"])
        df.to_excel("Subfamilias.xlsx", index=False)
        print("End Exportacion")


obj = GetSubfamilias()
listSubfamiliaIndustry = obj.get_subfamiliIndustry(tipo=4)
print(len(listSubfamiliaIndustry))
input("Continuar")
checkSubFamiliaSolmicro = obj.checkSubFamiliaSolmicro(listSubfamilia=listSubfamiliaIndustry)
input("Continuar")
obj.export_subFamilias_excel(subFamiliasList=checkSubFamiliaSolmicro)