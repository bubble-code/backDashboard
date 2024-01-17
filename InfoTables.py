from sqlalchemy import text
from Conexion import MainConexion
from datetime import datetime
import pandas as pd
from flask import jsonify
from json import loads, dumps


class SQLTableInfo:
    def __init__(self):
        self.conexion = MainConexion()
        self.tables_info = []

    def get_pk_table_info(self, engine, table_name):
        try:
            query = text(
                f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = '{table_name}' AND CONSTRAINT_NAME LIKE 'PK_%'"
            )
            result = engine.execute(query).fetchone()
            return result[0]
        except Exception as e:
            print("Error executing query: ", e)
            return ""

    def get_table_data(self, engine, table_name):
        try:
            query = text(f"SELECT * FROM {table_name}")
            with engine:
                result = engine.execute(query).fetchall()
                data_list = [row._asdict() for row in result]
            return data_list
        except Exception as e:
            print("Error getting data ", e)
            return []

    def get_data_comparar(self, table_name):
        db_prueba = self.get_table_data(self.conexion.Open_Conn_Solmicro(), table_name)
        db_favram = self.get_table_data(self.conexion.Open_Conn_Solmicro_New(), table_name)
        pk_prueba = self.get_pk_table_info(self.conexion.Open_Conn_Solmicro_New(), table_name)
        dt_prueba = pd.DataFrame(db_prueba)
        dt_favram = pd.DataFrame(db_favram)
        # Compara los DataFrames y encuentra las diferencias
        df_both_ways = pd.concat([dt_prueba, dt_favram]).drop_duplicates(keep=False)
        dict_both_ways = df_both_ways.to_dict(orient="records")
        clean_both_ways = self.clean_na_values(dict_both_ways)

        df_prueba_only = (dt_prueba.merge(dt_favram, how="left", indicator=True, on=[pk_prueba]).query('_merge == "left_only"').drop("_merge", axis=1))
        dict_prueba_only = df_prueba_only.to_dict(orient="records")
        clean_prueba_only = self.clean_na_values(dict_prueba_only)

        df_favram_only = (dt_favram.merge(dt_prueba, how="left", indicator=True, on=[pk_prueba]).query('_merge == "left_only"').drop("_merge", axis=1))
        dict_favram_only = df_favram_only.to_dict(orient="records")
        clean_favram_only = self.clean_na_values(dict_favram_only)

        result_dict = {
            "df_favram": clean_favram_only,
            "df_prueba": clean_prueba_only,
            "df_both_ways": clean_both_ways,
        }

        return result_dict

    def clean_na_values(self, data_list):
        cleaned_list = []
        for data_dict in data_list:
            cleaned_dict = {}
            for key, value in data_dict.items():
                if isinstance(value, list):
                    cleaned_dict[key] = [self.clean_na_values(item) if pd.notna(item) else None for item in value]
                elif isinstance(value, dict):
                    cleaned_dict[key] = self.clean_na_values(value)
                elif pd.isna(value):
                    cleaned_dict[key] = None
                else:
                    cleaned_dict[key] = value
            cleaned_list.append(cleaned_dict)
        return cleaned_list

    def ipdate_into_aleNameTablas(self, table_name):
        conn = None
        try:
            conn = self.conexion.Open_Conn_Solmicro()
            if conn:
                query = text(
                    f"UPDATE  aleNameTablas SET  Completed = 1, UltimaActual = '{datetime.now()}' WHERE Name =N'{table_name}'"
                )
                conn.execute(query)
                conn.commit()
        except Exception as e:
            print(f"Error inserting into aleNameTablas for table{table_name}:{e}")
        finally:
            if conn:
                conn.close()

    def update_checked(self, table_name):
        conn = None
        try:
            conn = self.conexion.Open_Conn_Solmicro()
            if conn:
                query = text(
                    f"UPDATE aleNameTablas SET Checked = 1 where Name = N'{table_name}'"
                )
                conn.execute(query)
                conn.commit()
        except Exception as e:
            print("Error updating table", e)
        finally:
            if conn:
                conn.close()
