from sqlalchemy import create_engine, text, bindparam, Integer, select, func
from Conexion import MainConexion
from sqlalchemy.orm import sessionmaker
import pandas as pd

class ImportArticulos:
    def __init__(self):
        self.ruta_archivo = r'ArtFormateados2.xlsx' 
        self.hoja_excel = 'Sheet1'
        

    def getDatosArtIndustry(self, TipoArticulo =1):
        mainConexion = MainConexion()
        try:
            conn = mainConexion.Open_Conn_Industry()
            if conn:
                print("Get DatosArtIndustry")
                query = text(
                    f"SELECT MArticulo.CodigoArticulo, MArticulo.Descripcion, MArticulo.Familia, MArticulo.Subfamilia, MArticulo.UltimoPrecioCoste, MArticulo.PrecioCosteMedio, MArticulo.ProveedorHabitual, MArticulo.PlazoAprovisionam, MArticulo.PlazoSeguridad, MArticulo.SerieMinimaRentable, MArticulo.TipoArticulo, MArticulo.StockMinimo, MArticulo.StockMaximo, MArticulo.Existencia, MArticulo.UnidReservadas, MArticulo.UnidOrdenadas, MArticulo.Codigo2, MArticulo.Codigo3, MArticulo.FechaUltimaCompra, MArticulo.FechaUltimaEntrada, MArticulo.FechaUltimaSalida, MArticulo.FechaCreacion, MArticulo.PesoNeto, MArticulo.PesoBruto, MArticulo.UnidMedidaCompra, MArticulo.UnidMedidaVenta, MArticulo.UnidMedidaAlmacen, MArticulo.MultiploFabricacion, MArticulo.TipoEnvase, MArticulo.CantidadEnvase, MArticulo.NumPlano, MArticulo.CodigoMoldeMatriz, MArticulo.EstadoArticulo, MArticulo.UnidConverCompra, MArticulo.AlmacenDefecto, MArticulo.CodigoUltimoProv, MArticulo.Inventariable, MArticulo.UbicacionDefecto, MArticulo.FechaDeAlta, MArticulo.FechaUltimaModificacion, MArticulo.UsuarioAlta, MArticulo.UsuarioModificacion, MArticulo.Version, MArticulo.GuardaVersion, MArticulo.Descripcion2, MArticulo.SumatorioComponentes, MArticulo.UnidConverVenta, MArticulo.PrecioCosteStandard, MArticulo.PrecioCompra, MArticulo.PrecioCompraDivisa, MArticulo.CodigoMoneda, MArticulo.PorcIVA, MArticulo.PorcRecargo, MArticulo.ABC, MArticulo.Trazabilidad, MArticulo.CriterioAsignacionLote, MArticulo.NumeroSerie, MArticulo.DiasCuarentena, MArticulo.RevisionPlano, MArticulo.FechaUltimaRevisionPlano, MArticulo.UnidMedidasEnvase, MArticulo.MedidaEnvaseLargo, MArticulo.MedidaEnvaseAncho, MArticulo.MedidaEnvaseAlto, MArticulo.UnidVolumenEnvase, MArticulo.MedidaEnvaseVolumen, MArticulo.ClientePrincipal, MArticulo.ClienteExclusivo, MArticulo.PrecioHIFO, MArticulo.FechaPrecioHIFO, MArticulo.MultiploConsumo, MArticulo.LotificacionPropia, MArticulo.ValorNumeroSerie, MArticulo.CosteStandarMOE, MArticulo.PrecioVenta, MArticulo.IDDocumAdjuntos, MArticulo.MesesGarantia, MArticulo.SistemaDistribucionObjetivos, MArticulo.PorcComision, MArticulo.CodNomenclaturaCombinada, MArticulo.RegimenEstadisticoHabitual, MArticulo.NaturalezaTransaccionA, MArticulo.NaturalezaTransaccionB, MArticulo.CodUnidadSuplem, MArticulo.FactorConversionSuplem, MArticulo.ClaseArticulo, MArticulo.Plantilla, MArticulo.GeneradorPlantilla, MArticulo.CodigoEstructura, MArticulo.EjecucionEN15085, MArticulo.TipoImpuesto, MArticulo.TipoArticuloVariantes, MArticulo.MesesCaducidad, MArticulo.Contador, MArticulo.Generico, MArticulo.FijarCosteStandard, MArticulo.Despunte, MArticulo.PorcRecuperado, MArticulo.altCantidadPorLote, MArticulo.DiasCaducidad, MArticulo.Pantone, MArticulo.RAL, MArticulo.CodigoAdicionalIntrastat, MArticulo.ExcluirEnIntrastat, MArticulo.DiasCaducidadInterna, MArticulo.MesesCaducidadInterna, MArticulo.MinimoCompra, MArticulo.PorcIGIC, MArticulo.VersionDesc, MArticulo.AplicaRedondeo, MArticulo.DecimalesRedondeo, MArticulo.Kit, MArticulo.UltimoPrecioCosteConInd, MArticulo.ProductoECommerce, MArticulo.ProductoDestacadoECommerce, MArticulo.AplicarRedondeoAlza, MArticulo.NumOperacionesTotales, MArticulo.NumOperacionesSerieLarga, MArticulo.Notificaciones, MArticulo.CtrlLimitePrecioVenta, MArticulo.CodigoEstructura1, MArticulo.LoteEntrega, MArticulo.DiasAprovComprasMasLargo, REPLACE(MArticuloCuenta.CuentaCompras, ' ', '') + REPLACE(MArticuloCuenta.SubcuentaCompras, ' ', '') AS CCompra FROM MArticulo LEFT OUTER JOIN MArticuloCuenta ON MArticulo.CodigoArticulo = MArticuloCuenta.CodigoArticulo WHERE TipoArticulo = N'{TipoArticulo}'")
                result = conn.execute(query).fetchall()
                print("Completed")
                return result
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if conn:
                conn.close()

    def CheckArticuloSolmicro(self,listArticulos):
        mainConexion = MainConexion()
        resultados = []
        try:
            conn = mainConexion.Open_Conn_Solmicro()
            if conn:
                print("Check articulo in Solmicro")
                for articulo in listArticulos:
                    print(articulo[0])
                    query = text(f"SELECT top(1) IDArticulo FROM tbMaestroArticulo WHERE IDArticulo = N'{articulo[0]}' ")
                    result = conn.execute(query).fetchone()
                    if not result:
                        resultados.append(articulo)
                conn.commit()
                conn.close()
                print("Completado")
            return resultados
        except Exception as e:
            print("Error en la consulta:", e)
            return resultados
        
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
                    "CCCompra": linea[123] if linea[10] == 4 else None,
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
    
    @staticmethod
    def export_to_excel_art_desd_indus(data):
        print("Exporting")
        df = pd.DataFrame(data, columns=["IDArticulo",	"DescArticulo",	"IDContador",	"FechaAlta",	"IDEstado",	"IDTipo",	"IDFamilia",	"IDSubfamilia",	"CCVenta",	"CCExport",	"CCCompra",	"CCImport",	"CCVentaRegalo",	"CCGastoRegalo",	"CCStocks",	"IDTipoIva",	"IDPartidaEstadistica",	"IDUdInterna",	"IDUdVenta",	"IDUdCompra",	"PrecioEstandarA",	"PrecioEstandarB",	"FechaEstandar",	"UdValoracion",	"PesoNeto",	"PesoBruto",	"TipoEstructura",	"IDTipoEstructura",	"TipoRuta",	"IDTipoRuta",	"CodigoBarras",	"PuntoVerde",	"PVPMinimo",	"PorcentajeRechazo",	"Plazo",	"Volumen",	"RecalcularValoracion",	"CriterioValoracion",	"GestionStockPorLotes",	"PrecioUltimaCompraA",	"PrecioUltimaCompraB",	"FechaUltimaCompra",	"IDProveedorUltimaCompra",	"LoteMultiplo",	"CantMinSolicitud",	"CantMaxSolicitud",	"LimitarPetDia",	"IdArticuloConfigurado",	"ContRadical",	"IdFamiliaConfiguracion",	"PrecioBase",	"Configurable",	"FechaCreacionAudi",	"FechaModificacionAudi",	"UsuarioAudi",	"NivelPlano",	"StockNegativo",	"PlazoFabricacion",	"ParamMaterial",	"ParamTerminado",	"CapacidadDiaria",	"AplicarLoteMRP",	"NSerieObligatorio",	"PuntosMarketing",	"ValorPuntosMarketing",	"ValorReposicionA",	"ValorReposicionB",	"FechaValorReposicion",	"ControlRecepcion",	"IDEstadoHomologacion",	"IDArticuloFinal",	"GenerarOFArticuloFinal",	"IdDocumentoEspecificacion",	"NivelModificacionPlan",	"FechaModificacionNivelPlan",	"TipoFactAlquiler","Seguridad",	"Reglamentacion",	"SeguridadReglamentacion",	"DiasMinimosFactAlquiler",	"SinDtoEnAlquiler",	"SinSeguroEnAlquiler",	"NecesitaOperario",	"IDConcepto",	"CCVentaGRUPO",	"CCExportGRUPO",	"CCImportGRUPO",	"CCCompraGRUPO",	"FacturacionAsociadaMaq",	"FactTasaResiduos",	"NoImprimirEnFactura",	"IDArticuloContenedor",	"QContenedor",	"IDArticuloEmbalaje",	"QEmbalaje",	"Color",	"IDCaracteristicaArticulo1",	"IDCaracteristicaArticulo2",	"IDCaracteristicaArticulo3",	"IDCaracteristicaArticulo4",	"IDCaracteristicaArticulo5",	"IDArticuloPadre",	"TipoPrecio",	"IDTipoProducto",	"IDTipoMaterial",	"IDTipoSubMaterial",	"IDTipoEnvase",	"IDComerIndus",	"IDTipoIVAReducido",	"IDUdInterna2",	"Observaciones",	"PorcenIVANoDeducible",	"PrecioBaseConfigurado",	"Alias",	"IDCategoria",	"IDAnada",	"IDColorVino",	"IDCategoriaVino",	"IDFormato",	"IDMarcaComercial",	"IDEmpresa",	"RetencionIRPF",	"IncluirEnEMCS",	"ClaveDeclaracion",	"IDRegistroFitosanitario",	"RiquezaNPK",	"IDTipoAbono",	"IDTipoFertilizacion",	"ClaveProductoSilicie",	"TipoEnvaseSilicie",	"ExcluirSilicie",	"IDCalificacion",	"IDProductoVino",	"IDPaisOrigen",	"CodigoEstructura",	"Certif31",	"Ubicacion",	"Codigo3",	"Descripcion2",	"INFAPP",	"EJEN15085",	"TIPO15085",	"ExcluirCupos",	"IDCampanaCupoClasificacion",	"KGPlastico",	"KGPlasticoNR",	"ClaveProducto",	"GestionContraPedidoVenta",	"UsuarioCreacionAudi",	"Espesor",	"Activo",	"Venta"])
        df.to_excel("ImportArticulos04.xlsx", index=False)
        print("End Exportacion")


obj = ImportArticulos()
listSubfamiliaIndustry = obj.getDatosArtIndustry(TipoArticulo=4)
print(len(listSubfamiliaIndustry))
input("Continuar")
checkSubFamiliaSolmicro = obj.CheckArticuloSolmicro(listArticulos=listSubfamiliaIndustry)
print(len(checkSubFamiliaSolmicro))
input("Continuar")
articulosSerialilzados = obj.serializer(datos=checkSubFamiliaSolmicro)
input("Continuar")
obj.export_to_excel_art_desd_indus(data=articulosSerialilzados)