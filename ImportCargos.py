from Conexion import MainConexion
import pandas as pd

class MaestroCargoManager:
    def __init__(self, main_conexion):
        self.main_conexion = main_conexion

    def get_all_records(self):
        mainConexion = MainConexion()
        try:
            conn = self.main_conexion.Open_Conn_Solmicro()
            if conn:
                print ("Get Data")
                query = "SELECT * FROM tbMaestroCargo"
                result = pd.read_sql(query, conn)
                return result
        except Exception as e:
            print ("Query Error:", e)
            return None
        finally:
            if conn:
                conn.close()

    def save_to_excel(self, dataframe, excel_filename):
        try:
            dataframe.to_excel(excel_filename, index=False, sheet_name=self.main_conexion.hoja_excel)
            print(f"Registros guardados en el archivo Excel: {excel_filename}")
        except Exception as e:
            print("Error guardando en el archivo Excel:", e)


# Ejemplo de uso:
if __name__ == "__main__":
    main_conexion = MainConexion()
    maestro_cargo_manager = MaestroCargoManager(main_conexion)
    input("Creadas las instancias")

    # Obtener todos los registros de tbMaestroCargo
    records = maestro_cargo_manager.get_all_records()
    print(len(records))
    input("Cantidad de registros")

    if records is not None:
        # Guardar en un archivo Excel
        maestro_cargo_manager.save_to_excel(records, 'MaestroCargos.xlsx')