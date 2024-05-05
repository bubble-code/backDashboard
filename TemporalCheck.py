from sqlalchemy import create_engine, text
import pandas as pd

class HH:
    def __init__(self):
        self.server_industry = r'SERVIDOR'
        self.server_solmicro = r'srvsql'
        self.database_solmicro = 'SolmicroERP6_PruebasSub'
        self.database_solmicro_new = 'SolmicroERP6_Favram'
        self.database_industry = 'IPFavram'
        self.username_solmicro = 'sa'
        self.password_solmicro = 'Altai2021'
        self.password_industry = '71zl6p9h'
        self.connection_string_solmicro = create_engine(
            f'mssql+pyodbc://{self.username_solmicro}:{self.password_solmicro}@{self.server_solmicro}/{self.database_solmicro}?driver=SQL+Server')
        self.connection_string_solmicro_new = create_engine(
            f'mssql+pyodbc://{self.username_solmicro}:{self.password_solmicro}@{self.server_solmicro}/{self.database_solmicro_new}?driver=SQL+Server')
        self.connection_string_industry = create_engine(
            f'mssql+pyodbc://{self.username_solmicro}:{self.password_industry}@{self.server_industry}/{self.database_industry}?driver=SQL+Server')
    
    def Open_Conn_Solmicro(self):
        try:
            connection = self.connection_string_solmicro.connect()
            return connection
        except Exception as e:
            print("Error opening connection: ", e)
    
    def Open_Conn_Industry(self):
        try:
            self.connection = self.connection_string_industry.connect()
            return self.connection
        except Exception as e:
            print("Error opening connection: ", e)

    def get_Industry(self):
        try:
            query = text(
                f"select m.CodigoArticulo from MLotes as m inner join MArticulo as ma on m.CodigoArticulo = ma.CodigoArticulo where (m.Stock>0) and (m.TipoArticulo=4) and (ma.TipoArticulo = 4) and (ma.Familia in (N'4015',N'4016',N'4017'))"
            )
            conn = self.Open_Conn_Industry()
            with conn:
                return pd.read_sql_query(query,conn)
        except Exception as e:
            print("Error executing query: ", e)
            return ""
        finally:
            if conn:
                conn.close()
    
    def get_solmicro(self):
        try:
            query = text(f"SELECT IDArticulo AS CodigoArticulo FROM tbArticuloAlmacenLote")
            conn = self.Open_Conn_Solmicro()
            return pd.read_sql_query(query,conn)
        except Exception as e:
            print("Error executing query: ", e)
            return ""
        finally:
            if conn:
                conn.close()
        

oo = HH()
input('instancia creada: ')
rr = oo.get_Industry()
input("Terminado Get data from Industry")
ff = oo.get_solmicro()
input("Terminado Get data from Solmicro")
df_prueba_only = (rr.merge(ff, how="left", indicator=True, on=["CodigoArticulo"]).query('_merge == "left_only"').drop("_merge", axis=1))
print(df_prueba_only)
        