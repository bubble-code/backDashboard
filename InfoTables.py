from sqlalchemy import text
from Conexion import MainConexion


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
                    f"SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_name LIKE '%{keyword}%'")
                result = conn.execute(query).fetchall()
                return [row[0] for row in result]
        except Exception as e:
            print("Error getting table names: ", e)
            return []
        finally:
            if conn:
                conn.close()

    def get_data(self, nameTable):
        conn = None
        try:
            conn = self.conexion.Open_Conn_Solmicro()
            if conn:
                query = text(f"SELECT top(10) * FROM {nameTable}")
                result = conn.execute(query).fetchall()
                data_list = [{"key": i, **row._asdict()} for i, row in enumerate(result)]
                return data_list
        except Exception as e:
            print("Error getting data ", e)
            return []
        finally:
            if conn:
                conn.close()
