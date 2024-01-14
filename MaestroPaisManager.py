from Conexion import MainConexion
from models.MaestroPais import MaestroPais
import pandas as pd

class MaestroPaisManager:
    def __init__(self, main_conexion, model_class):
        self.main_conexion = main_conexion
        self.model_class = model_class

    def get_all_records(self):
        conn = None
        try:
            conn = self.main_conexion._open_session_solmicro()
            if conn:
                print ("Get Data")
                # session = sessionmaker(bind=conn)()
                records = conn.query(self.model_class).all()
                return records
        except Exception as e:
            print("Error obteniendo registros:", e)
            return None
        finally:
            if conn:
                conn.close()

    def save_to_excel(self, records, excel_filename):
        try:
            data = []
            for record in records:
                data.append({column.name: getattr(record, column.name) for column in self.model_class.__table__.columns})

            dataframe = pd.DataFrame(data)
            dataframe.to_excel(excel_filename, index=False, sheet_name=self.main_conexion.hoja_excel)
            print(f"Registros guardados en el archivo Excel: {excel_filename}")
        except Exception as e:
            print("Error guardando en el archivo Excel:", e)

# Ejemplo de uso:
# if __name__ == "__main__":
#     main_conexion = MainConexion()
#     maestro_pais_manager = MaestroPaisManager(main_conexion, MaestroPais)
#     input("Creadas las instancias")
#     # Obtener todos los registros de tbMaestroPais
#     records = maestro_pais_manager.get_all_records()
#     # print(len(records))
#     input("Cantidad de registros")

#     if records is not None:
#         # Guardar en un archivo Excel
#         maestro_pais_manager.save_to_excel(records, 'MaestroPais.xlsx')
