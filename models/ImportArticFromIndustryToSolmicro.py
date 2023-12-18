from sqlalchemy import create_engine, text, bindparam, Integer, select
from sqlalchemy.orm import sessionmaker
import pandas as pd
from Subfamilia import MaestroSubfamilia


class DatosArticulos:
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

    

    def GetSubFamilias(self,familia,subList):
        resultados = []
        try:
            conn = self.Open_Conn_Solmicro()
            if conn:
                print("Get SubFamilias")
                for subF in subList:             
                    query = text(f"SELECT IDTipo,IDFamilia, IDSubfamilia, DescSubfamilia, FechaCreacionAudi, FechaModificacionAudi, UsuarioAudi, NumCorrelativo, Precinta, PorcMermaMaxima, IDCodigo, IDConfig, DescConfig, PorcRecepcionMaximo, ConsejoRegulador, SeguimientoPrecinta, UsuarioCreacionAudi FROM tbMaestroSubfamilia WHERE (IDFamilia = N'{familia}' AND IDSubfamilia = N'{subF}')")
                    result = conn.execute(query).fetchall()
                    if not result:
                        resultados.append(subF)
                print("Completed")
                return resultados
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()
    # @classmethod
    def GetCheckSubFamiliasSolmicro(self, IDTipo=None, IDFamilia=None, IDSubfamilia=None, session=None):
        Session = sessionmaker(bind=self.connection_string_solmicro)
        session = Session()
        stmt = session.query(MaestroSubfamilia)
        # if IDTipo is not None:
        #     stmt = stmt.filter(MaestroSubfamilia.IDTipo == IDTipo)
        # if IDFamilia is not None:
        #     stmt = stmt.filter(MaestroSubfamilia.IDFamilia == IDFamilia)
        # if IDSubfamilia is not None:
        #     stmt = stmt.filter(MaestroSubfamilia.IDSubfamilia == IDSubfamilia)

        query =  stmt.scalar_subquery()
        # registros = query.all()
        session.close()
        return query
    
    def check_subfamilia(self):
        resultados = []
        Session = sessionmaker(bind=self.connection_string_solmicro)
        session = Session()
        # for item in lista_subfamilia:
        #     result= self.GetCheckSubFamiliasSolmicro(IDFamilia="VENTACLIEN",session=session)
        #     if result:
        #         resultados.append(result)
        return self.GetCheckSubFamiliasSolmicro(session=session)


    
    
    def GetColumnExcel(self,nameColumn):
        print("Obteniendo datos desde Excel")
        try:
            datos_excel = pd.read_excel(self.ruta_archivo, sheet_name=self.hoja_excel)
            columna_especifica = datos_excel[nameColumn] 
            art_ids = list(set(item for item in columna_especifica if pd.notnull(item)))
            print("Completed")
            return art_ids
        except Exception as e:
            print("Error Excel: ",e)


    def ExcelArtProveedor(self,listProvedore):
        try:
            datos_excel = pd.read_excel(self.ruta_archivo, sheet_name=self.hoja_excel)
            ProveedorHabitual = datos_excel["ProveedorHabitual"]
            CodigoArticulo = datos_excel["CodigoArticulo"]
            filtered_data = datos_excel[ProveedorHabitual.isin(listProvedore)]
            art_codigos_proveedores = list(zip(filtered_data["CodigoArticulo"], round(filtered_data["ProveedorHabitual"])))
            return art_codigos_proveedores
        except Exception as e:
            print("Error Excel: ",e)


    
    @staticmethod
    def export_subFamilias_excel(subFamiliasList):
        print("Exporting")
        df = pd.DataFrame(subFamiliasList,columns=["SubFamilias"])
        df.to_excel("ArtFormateados3.xlsx", index=False)
        print("End Exportacion")


print("ObjImport")
# artIndustry = ObjImport.getDatosArtIndustry()
# input("Continue")
# artSerializerSolmicro = ObjImport.serializer(artIndustry)
# input("Continue")
# ObjImport.export_to_excel_art_desd_indus(artSerializerSolmicro)
# input("Continue")
# idFamiliasList = ObjImport.GetColumnExcel(nameColumn="SubFamilias")
# input("Continue")
# subFamiliasFrom_Solmicro = ObjImport.GetSubFamilias(familia="VENTACLIEN", subList=idFamiliasList)
# input("Continue")
# ObjImport.export_subFamilias_excel(subFamiliasList=subFamiliasFrom_Solmicro)
input("Continue")
ObjImport = DatosArticulos()
result = ObjImport.GetCheckSubFamiliasSolmicro()
for registro in result:
    print(f"IDTipo: {registro.IDTipo}, IDFamilia: {registro.IDFamilia}, IDSubfamilia: {registro.IDSubfamilia}, DescSubfamilia: {registro.DescSubfamilia}")
