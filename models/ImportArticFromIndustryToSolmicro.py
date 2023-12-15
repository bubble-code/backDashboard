from sqlalchemy import create_engine, text, bindparam, Integer
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

    def getDatosArtIndustry(self):
        try:
            conn = self.Open_Conn_Industry()
            if conn:
                print("Get DatosArtIndustry")
                query = text(
                    f"SELECT CodigoArticulo, Descripcion, Familia, Subfamilia, UltimoPrecioCoste, PrecioCosteMedio, ProveedorHabitual, PlazoAprovisionam, PlazoSeguridad, SerieMinimaRentable, TipoArticulo, StockMinimo,StockMaximo, Existencia, UnidReservadas, UnidOrdenadas, Codigo2, Codigo3, FechaUltimaCompra, FechaUltimaEntrada, FechaUltimaSalida, FechaCreacion, PesoNeto, PesoBruto, UnidMedidaCompra, UnidMedidaVenta,UnidMedidaAlmacen, MultiploFabricacion, TipoEnvase, CantidadEnvase, NumPlano, CodigoMoldeMatriz, EstadoArticulo, UnidConverCompra, AlmacenDefecto, CodigoUltimoProv, Inventariable, UbicacionDefecto, FechaDeAlta, FechaUltimaModificacion, UsuarioAlta, UsuarioModificacion, Version, GuardaVersion, Descripcion2, SumatorioComponentes, UnidConverVenta, PrecioCosteStandard, PrecioCompra, PrecioCompraDivisa, CodigoMoneda,PorcIVA, PorcRecargo, ABC, Trazabilidad, CriterioAsignacionLote, NumeroSerie, DiasCuarentena, RevisionPlano, FechaUltimaRevisionPlano, UnidMedidasEnvase, MedidaEnvaseLargo, MedidaEnvaseAncho, MedidaEnvaseAlto, UnidVolumenEnvase, MedidaEnvaseVolumen, ClientePrincipal, ClienteExclusivo, PrecioHIFO, FechaPrecioHIFO, MultiploConsumo, LotificacionPropia, ValorNumeroSerie, CosteStandarMOE, PrecioVenta, IDDocumAdjuntos,MesesGarantia, SistemaDistribucionObjetivos, PorcComision, CodNomenclaturaCombinada, RegimenEstadisticoHabitual, NaturalezaTransaccionA, NaturalezaTransaccionB, CodUnidadSuplem, FactorConversionSuplem, ClaseArticulo, Plantilla, GeneradorPlantilla, CodigoEstructura, EjecucionEN15085, TipoImpuesto, TipoArticuloVariantes, MesesCaducidad, Contador, Generico, FijarCosteStandard, Despunte, PorcRecuperado, altCantidadPorLote,DiasCaducidad, Pantone, RAL, CodigoAdicionalIntrastat, ExcluirEnIntrastat, DiasCaducidadInterna, MesesCaducidadInterna, MinimoCompra, PorcIGIC, VersionDesc, AplicaRedondeo, DecimalesRedondeo, Kit, UltimoPrecioCosteConInd, ProductoECommerce, ProductoDestacadoECommerce, AplicarRedondeoAlza, NumOperacionesTotales, NumOperacionesSerieLarga, Notificaciones, CtrlLimitePrecioVenta, CodigoEstructura1,LoteEntrega, DiasAprovComprasMasLargo FROM MArticulo WHERE TipoArticulo = 1")
                result = conn.execute(query).fetchall()
                print("Completed")
                return result
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()

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
        query =  session.query(MaestroSubfamilia).yield_per(100)
        registros = query.all()
        session.close()
        return registros
    
    def check_subfamilia(self):
        resultados = []
        Session = sessionmaker(bind=self.connection_string_solmicro)
        session = Session()
        # for item in lista_subfamilia:
        #     result= self.GetCheckSubFamiliasSolmicro(IDFamilia="VENTACLIEN",session=session)
        #     if result:
        #         resultados.append(result)
        return self.GetCheckSubFamiliasSolmicro(session=session)


    def serializer(self, datos):
        result = []
        print("Serializing")
        for linea in datos:
            result.append(
                {
                    "IDArticulo": linea[0],
                    "DescArticulo": linea[1],
                    "IDContador": None,
                    "FechaAlta": "2023-12-15 00:00:00.383",
                    "IDEstado": 0,
                    "IDTipo": linea[10],
                    "IDFamilia": "VENTACLIEN" if linea[10] == 1 else linea[2],
                    "IDSubfamilia": linea[2] if linea[10] == 1 else linea[3],
                    "CCVenta": "70000000" if linea[10] == 1 else None,
                    "CCExport": None,
                    "CCCompra": "60700006" if linea[10] == 4 else None,
                    "CCImport": None,
                    "CCVentaRegalo": None,
                    "CCStocks": None,
                    "IDTipoIva": "NOR",
                    "IDPartidaEstadistica": None,
                    "IDUdInterna": linea[26],
                    "IDUdVenta": linea[25],
                    "IDUdCompra": linea[24],
                    "PrecioEstandarA": linea[47],
                    "PrecioEstandarB": linea[47],
                    "FechaEstandar": "2023-12-15 00:00:00.383",
                    "UdValoracion": 1,
                    "PesoNeto": linea[22],
                    "PesoBruto": linea[23],
                    "TipoEstructura": 0,
                    "IDTipoEstructura": None,
                    "TipoRuta": 0,
                    "IDTipoRuta": None,
                    "CodigoBarras": None,
                    "PuntoVerde": 0.00000000,
                    "PVPMinimo": linea[74],
                    "PorcentajeRechazo": 0,
                    "Plazo": linea[7],
                    "Volumen": 0,
                    "RecalcularValoracion": 1,
                    "CriterioValoracion": 0,
                    "GestionStockPorLotes": 0,
                    "PrecioUltimaCompraA": 0.00000000,
                    "PrecioUltimaCompraB": 0.00000000,
                    "FechaUltimaCompra": None,
                    "IDProveedorUltimaCompra": None,
                    "LoteMultiplo": 0,
                    "CantMinSolicitud": 0,
                    "CantMaxSolicitud": 0,
                    "LimitarPetDia": 0,
                    "IdArticuloConfigurado": None,
                    "ContRadical": None,
                    "IdFamiliaConfiguracion": None,
                    "PrecioBase": linea[74],
                    "Configurable": 0,
                    "FechaCreacionAudi": "2023-12-15 00:00:00.383",
                    "FechaModificacionAudi": "2023-12-15 00:00:00.383",
                    "UsuarioAudi": f"favram\\a.obregon",
                    "NivelPlano": linea[30],
                    "StockNegativo": 0,
                    "PlazoFabricacion": linea[7],
                    "ParamMaterial": 3 if linea[10] == 1 else None,
                    "ParamTerminado": 1 if linea[10] == 1 else None,
                    "ParamTerminado": 0.00000000,
                    "AplicarLoteMRP": 0,
                    "NSerieObligatorio": 0,
                    "PuntosMarketing": 0,
                    "ValorPuntosMarketing": 0,
                    "ValorReposicionA": 0.00000000,
                    "ValorReposicionB": 0.00000000,
                    "FechaValorReposicion": None,
                    "ControlRecepcion": 0,
                    "IDEstadoHomologacion": None,
                    "IDArticuloFinal": None,
                    "GenerarOFArticuloFinal": 0,
                    "IdDocumentoEspecificacion": None,
                    "NivelModificacionPlan": None,
                    "FechaModificacionNivelPlan": None,
                    "TipoFactAlquiler": 0,
                    "Seguridad": 0,
                    "Reglamentacion": 0,
                    "SeguridadReglamentacion": 0,
                    "DiasMinimosFactAlquiler": 0,
                    "SinDtoEnAlquiler": 0,
                    "SinSeguroEnAlquiler": 0,
                    "NecesitaOperario": 0,
                    "IDConcepto": None,
                    "CCVentaGRUPO": None,
                    "CCExportGRUPO": None,
                    "CCImportGRUPO": None,
                    "CCCompraGRUPO": None,
                    "FacturacionAsociadaMaq": 0,
                    "FactTasaResiduos": 0,
                    "NoImprimirEnFactura": 0,
                    "IDArticuloContenedor": None,
                    "QContenedor": None,
                    "IDArticuloEmbalaje": None,
                    "QEmbalaje": None,
                    "Color": None,
                    "IDCaracteristicaArticulo1": None,
                    "IDCaracteristicaArticulo2": None,
                    "IDCaracteristicaArticulo3": None,
                    "IDCaracteristicaArticulo4": None,
                    "IDCaracteristicaArticulo5": None,
                    "IDArticuloPadre": None,
                    "TipoPrecio": None,
                    "IDTipoProducto": None,
                    "IDTipoMaterial": None,
                    "IDTipoSubMaterial": None,
                    "IDTipoEnvase": None,
                    "IDComerIndus": None,
                    "IDTipoIVAReducido": None,
                    "IDUdInterna2": None,
                    "Observaciones": None,
                    "PorcenIVANoDeducible": None,
                    "PrecioBaseConfigurado": None,
                    "Alias": None,
                    "IDCategoria": None,
                    "IDAnada": None,
                    "IDColorVino": None,
                    "IDCategoriaVino": None,
                    "IDFormato": None,
                    "IDMarcaComercial": None,
                    "IDEmpresa": None,
                    "INFAPNecesitaOperario": None,
                    "RetencionIRPF": 1,
                    "IncluirEnEMCS": 0,
                    "ClaveDeclaracion": None,
                    "IDRegistroFitosanitario": None,
                    "RiquezaNPK": None,
                    "IDTipoAbono": None,
                    "IDTipoFertilizacion": None,
                    "ClaveProductoSilicie": None,
                    "TipoEnvaseSilicie": None,
                    "ExcluirSilicie": 0,
                    "IDCalificacion": None,
                    "IDProductoVino": None,
                    "IDPaisOrigen": None,
                    "CodigoEstructura": None,
                    "Certif31": None,
                    "Ubicacion": None,
                    "Codigo3": None,
                    "Descripcion2": None,
                    "INFAPP": None,
                    "EJEN15085": None,
                    "TIPO15085": None,
                    "TIPO15085": None,
                    "ExcluirCupos": 0,
                    "IDCampanaCupoClasificacion": None,
                    "KGPlastico": None,
                    "KGPlasticoNR": None,
                    "ClaveProducto": None,
                    "GestionContraPedidoVenta": 0,
                    "UsuarioCreacionAudi": None,
                    "Espesor": None,
                    "Activo": 1,
                    "Venta": 1
                }
            )
        print("End Serializado")
        return result
    
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
    def export_to_excel_art_desd_indus(data):
        print("Exporting")
        df = pd.DataFrame(data, columns=["IDArticulo",	"DescArticulo",	"IDContador",	"FechaAlta",	"IDEstado",	"IDTipo",	"IDFamilia",	"IDSubfamilia",	"CCVenta",	"CCExport",	"CCCompra",	"CCImport",	"CCVentaRegalo",	"CCGastoRegalo",	"CCStocks",	"IDTipoIva",	"IDPartidaEstadistica",	"IDUdInterna",	"IDUdVenta",	"IDUdCompra",	"PrecioEstandarA",	"PrecioEstandarB",	"FechaEstandar",	"UdValoracion",	"PesoNeto",	"PesoBruto",	"TipoEstructura",	"IDTipoEstructura",	"TipoRuta",	"IDTipoRuta",	"CodigoBarras",	"PuntoVerde",	"PVPMinimo",	"PorcentajeRechazo",	"Plazo",	"Volumen",	"RecalcularValoracion",	"CriterioValoracion",	"GestionStockPorLotes",	"PrecioUltimaCompraA",	"PrecioUltimaCompraB",	"FechaUltimaCompra",	"IDProveedorUltimaCompra",	"LoteMultiplo",	"CantMinSolicitud",	"CantMaxSolicitud",	"LimitarPetDia",	"IdArticuloConfigurado",	"ContRadical",	"IdFamiliaConfiguracion",	"PrecioBase",	"Configurable",	"FechaCreacionAudi",	"FechaModificacionAudi",	"UsuarioAudi",	"NivelPlano",	"StockNegativo",	"PlazoFabricacion",	"ParamMaterial",	"ParamTerminado",	"CapacidadDiaria",	"AplicarLoteMRP",	"NSerieObligatorio",	"PuntosMarketing",	"ValorPuntosMarketing",	"ValorReposicionA",	"ValorReposicionB",	"FechaValorReposicion",	"ControlRecepcion",	"IDEstadoHomologacion",	"IDArticuloFinal",	"GenerarOFArticuloFinal",	"IdDocumentoEspecificacion",	"NivelModificacionPlan",	"FechaModificacionNivelPlan",	"TipoFactAlquiler","Seguridad",	"Reglamentacion",	"SeguridadReglamentacion",	"DiasMinimosFactAlquiler",	"SinDtoEnAlquiler",	"SinSeguroEnAlquiler",	"NecesitaOperario",	"IDConcepto",	"CCVentaGRUPO",	"CCExportGRUPO",	"CCImportGRUPO",	"CCCompraGRUPO",	"FacturacionAsociadaMaq",	"FactTasaResiduos",	"NoImprimirEnFactura",	"IDArticuloContenedor",	"QContenedor",	"IDArticuloEmbalaje",	"QEmbalaje",	"Color",	"IDCaracteristicaArticulo1",	"IDCaracteristicaArticulo2",	"IDCaracteristicaArticulo3",	"IDCaracteristicaArticulo4",	"IDCaracteristicaArticulo5",	"IDArticuloPadre",	"TipoPrecio",	"IDTipoProducto",	"IDTipoMaterial",	"IDTipoSubMaterial",	"IDTipoEnvase",	"IDComerIndus",	"IDTipoIVAReducido",	"IDUdInterna2",	"Observaciones",	"PorcenIVANoDeducible",	"PrecioBaseConfigurado",	"Alias",	"IDCategoria",	"IDAnada",	"IDColorVino",	"IDCategoriaVino",	"IDFormato",	"IDMarcaComercial",	"IDEmpresa",	"RetencionIRPF",	"IncluirEnEMCS",	"ClaveDeclaracion",	"IDRegistroFitosanitario",	"RiquezaNPK",	"IDTipoAbono",	"IDTipoFertilizacion",	"ClaveProductoSilicie",	"TipoEnvaseSilicie",	"ExcluirSilicie",	"IDCalificacion",	"IDProductoVino",	"IDPaisOrigen",	"CodigoEstructura",	"Certif31",	"Ubicacion",	"Codigo3",	"Descripcion2",	"INFAPP",	"EJEN15085",	"TIPO15085",	"ExcluirCupos",	"IDCampanaCupoClasificacion",	"KGPlastico",	"KGPlasticoNR",	"ClaveProducto",	"GestionContraPedidoVenta",	"UsuarioCreacionAudi",	"Espesor",	"Activo",	"Venta"])
        df.to_excel("ArtFormateados.xlsx", index=False)
        print("End Exportacion")
    
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
