from sqlalchemy import text
from Conexion import MainConexion
from datetime import datetime


class SQLTableInfo:
    def __init__(self):
        self.conexion = MainConexion()
        self.tables_info = []

    def get_tables_with_keyword(self, keyword="maestro"):
        conn = None
        try:
            conn = self.conexion.Open_Conn_Solmicro()
            if conn:
                query = text(
                    f"SELECT * FROM aleNameTablas")
                result = conn.execute(query).fetchall()
                return [row._asdict() for row in result]
        except Exception as e:
            print("Error getting table names: ", e)
            return []
        finally:
            if conn:
                conn.close()
    
    def ipdate_into_aleNameTablas(self, table_name):
        conn = None
        try:
            conn = self.conexion.Open_Conn_Solmicro()
            if conn:
                query = text(f"UPDATE  aleNameTablas SET  Completed = 1, UltimaActual = '{datetime.now()}' WHERE Name =N'{table_name}'")
                conn.execute(query)
                conn.commit()
        except Exception as e:
            print(f"Error inserting into aleNameTablas for table{table_name}:{e}")
        finally:
            if conn:
                conn.close()

    def get_data(self, nameTable):
        conn = None
        try:
            conn = self.conexion.Open_Conn_Solmicro()
            if conn:
                query = text(f"SELECT * FROM {nameTable}")
                result = conn.execute(query).fetchall()
                data_list = [{"key": i, **row._asdict()} for i, row in enumerate(result)]
                return data_list
        except Exception as e:
            print("Error getting data ", e)
            return []
        finally:
            if conn:
                conn.close()

    def get_data_new(self, nameTable):
        conn = None
        try:
            conn = self.conexion.Open_Conn_Solmicro_New()
            if conn:
                query = text(f"SELECT * FROM {nameTable}")
                result = conn.execute(query).fetchall()
                data_list = [{"key": i, **row._asdict()} for i, row in enumerate(result)]
                return data_list
        except Exception as e:
            print("Error getting data ", e)
            return []
        finally:
            if conn:
                conn.close()
