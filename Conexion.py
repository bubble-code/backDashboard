from sqlalchemy import create_engine, text, bindparam, Integer, select
from sqlalchemy.orm import sessionmaker


class MainConexion:
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

    def _open_session_solmicro(self):
        return sessionmaker(bind= self.Open_Conn_Solmicro())()
    
    def _open_session_industry(self):
        return sessionmaker(bind= self.Open_Conn_Industry())()

    def RunProcedure(self,rango):
        conn = None
        try:
            conn = self.Open_Conn_Solmicro()
            if conn:
                for dato in range(rango):
                    query = text("EXEC xAutonumericValue;")
                    conn.execute(query)
                    conn.commit()
        except Exception as e:
            print("Error ejecutando el procedimiento almacenado:", e)
            return None
        finally:
            if conn:
                conn.close()

    def GetAutonumericValue(self):
        conn = None
        try:
            conn = self.Open_Conn_Solmicro()
            if conn:
                query = text("SELECT autonumber FROM  ale_autoNumber")
                result = conn.execute(query).fetchall()
                final_result = [ value for row in result for value in row ]
                return final_result
        except Exception as e:
            print("Error ejecutando el procedimiento almacenado:", e)
            return None
        finally:
            if conn:
                conn.close()