import pandas as pd
import os

class CExcel:
    
    def Create_path(self, ruta_archivo):
        return os.path.join(ruta_archivo)

    def CargarExcel(self, ruta_archivo, hoja_excel, columnas):
        try:
            path_excel = os.path.join('Excel', ruta_archivo)
            datos_excel = pd.read_excel(path_excel, sheet_name=hoja_excel)
            columna_especifica = datos_excel[columnas]
            # art_ids = list(set(item for item in columna_especifica))
            return columna_especifica
        except Exception as e:
            print("Error Excel: ", e)

    def export_to_excel(self,name,data,columnas):
        print("Exporting")
        df = pd.DataFrame(data, columns=columnas)
        df.to_excel(name, index=False)
        print("End Exportacion")