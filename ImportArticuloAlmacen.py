from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from models.MaestroArticuloAlmacen import MaestroArticuloAlmacen
from Conexion import MainConexion
from CExcel import CExcel


class MaestroArticuloAlmacenManager:
    def __init__(self):
        self.main_conexion = MainConexion()

    def getAll(self):
        session_solmicro = self.main_conexion._open_session_solmicro()
        return session_solmicro.query(MaestroArticuloAlmacen).all()

    def filter_by_id(self, id):
        try:
            session_solmicro = self.main_conexion._open_session_solmicro()
            return session_solmicro.query(MaestroArticuloAlmacen).filter_by(IDArticulo=id).all()
        except Exception as e:
            print("Error en la consulta: " + str(e))
        finally:
            if session_solmicro:
                session_solmicro.close()
                

    def df_excel(self):
        excel = CExcel()
        df_datos = excel.CargarExcel(
            ruta_archivo=f"MissingStructure.xlsx", hoja_excel="Sheet1", columnas=["IDEstrComp", "IDArticulo", "IDComponente"])
        return df_datos

    def get_data_from_industry(self, data):
        try:
            session_industry = self.main_conexion._open_session_industry()
            # data_set = list(set(data["IDComponente"]))
            resultado = []
            if session_industry:
                print("Get DatosArtIndustry")
                for item in data:
                    query = text(
                        f"SELECT MArticulo.CodigoArticulo, MArticulo.Descripcion, MArticulo.Familia, MArticulo.Subfamilia, MArticulo.UltimoPrecioCoste, MArticulo.PrecioCosteMedio, MArticulo.ProveedorHabitual, MArticulo.PlazoAprovisionam, MArticulo.PlazoSeguridad, MArticulo.SerieMinimaRentable, MArticulo.TipoArticulo, MArticulo.StockMinimo, MArticulo.StockMaximo, MArticulo.Existencia, MArticulo.UnidReservadas, MArticulo.UnidOrdenadas, MArticulo.Codigo2, MArticulo.Codigo3, MArticulo.FechaUltimaCompra, MArticulo.FechaUltimaEntrada, MArticulo.FechaUltimaSalida, MArticulo.FechaCreacion, MArticulo.PesoNeto, MArticulo.PesoBruto, MArticulo.UnidMedidaCompra, MArticulo.UnidMedidaVenta, MArticulo.UnidMedidaAlmacen, MArticulo.MultiploFabricacion, MArticulo.TipoEnvase, MArticulo.CantidadEnvase, MArticulo.NumPlano, MArticulo.CodigoMoldeMatriz, MArticulo.EstadoArticulo, MArticulo.UnidConverCompra, MArticulo.AlmacenDefecto, MArticulo.CodigoUltimoProv, MArticulo.Inventariable, MArticulo.UbicacionDefecto, MArticulo.FechaDeAlta, MArticulo.FechaUltimaModificacion, MArticulo.UsuarioAlta, MArticulo.UsuarioModificacion, MArticulo.Version, MArticulo.GuardaVersion, MArticulo.Descripcion2, MArticulo.SumatorioComponentes, MArticulo.UnidConverVenta, MArticulo.PrecioCosteStandard, MArticulo.PrecioCompra, MArticulo.PrecioCompraDivisa, MArticulo.CodigoMoneda, MArticulo.PorcIVA, MArticulo.PorcRecargo, MArticulo.ABC, MArticulo.Trazabilidad, MArticulo.CriterioAsignacionLote, MArticulo.NumeroSerie, MArticulo.DiasCuarentena, MArticulo.RevisionPlano, MArticulo.FechaUltimaRevisionPlano, MArticulo.UnidMedidasEnvase, MArticulo.MedidaEnvaseLargo, MArticulo.MedidaEnvaseAncho, MArticulo.MedidaEnvaseAlto, MArticulo.UnidVolumenEnvase, MArticulo.MedidaEnvaseVolumen, MArticulo.ClientePrincipal, MArticulo.ClienteExclusivo, MArticulo.PrecioHIFO, MArticulo.FechaPrecioHIFO, MArticulo.MultiploConsumo, MArticulo.LotificacionPropia, MArticulo.ValorNumeroSerie, MArticulo.CosteStandarMOE, MArticulo.PrecioVenta, MArticulo.IDDocumAdjuntos, MArticulo.MesesGarantia, MArticulo.SistemaDistribucionObjetivos, MArticulo.PorcComision, MArticulo.CodNomenclaturaCombinada, MArticulo.RegimenEstadisticoHabitual, MArticulo.NaturalezaTransaccionA, MArticulo.NaturalezaTransaccionB, MArticulo.CodUnidadSuplem, MArticulo.FactorConversionSuplem, MArticulo.ClaseArticulo, MArticulo.Plantilla, MArticulo.GeneradorPlantilla, MArticulo.CodigoEstructura, MArticulo.EjecucionEN15085, MArticulo.TipoImpuesto, MArticulo.TipoArticuloVariantes, MArticulo.MesesCaducidad, MArticulo.Contador, MArticulo.Generico, MArticulo.FijarCosteStandard, MArticulo.Despunte, MArticulo.PorcRecuperado, MArticulo.altCantidadPorLote, MArticulo.DiasCaducidad, MArticulo.Pantone, MArticulo.RAL, MArticulo.CodigoAdicionalIntrastat, MArticulo.ExcluirEnIntrastat, MArticulo.DiasCaducidadInterna, MArticulo.MesesCaducidadInterna, MArticulo.MinimoCompra, MArticulo.PorcIGIC, MArticulo.VersionDesc, MArticulo.AplicaRedondeo, MArticulo.DecimalesRedondeo, MArticulo.Kit, MArticulo.UltimoPrecioCosteConInd, MArticulo.ProductoECommerce, MArticulo.ProductoDestacadoECommerce, MArticulo.AplicarRedondeoAlza, MArticulo.NumOperacionesTotales, MArticulo.NumOperacionesSerieLarga, MArticulo.Notificaciones, MArticulo.CtrlLimitePrecioVenta, MArticulo.CodigoEstructura1, MArticulo.LoteEntrega, MArticulo.DiasAprovComprasMasLargo, REPLACE(MArticuloCuenta.CuentaCompras, ' ', '') + REPLACE(MArticuloCuenta.SubcuentaCompras, ' ', '') AS CCompra FROM MArticulo LEFT OUTER JOIN MArticuloCuenta ON MArticulo.CodigoArticulo = MArticuloCuenta.CodigoArticulo WHERE MArticulo.CodigoArticulo = N'{item}'")
                    result = session_industry.execute(query).fetchone()
                    if result:
                        resultado.append(result)
                print("Completed")
                session_industry.commit()
                session_industry.close()
            return resultado
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if session_industry:
                session_industry.close()

    def serializar(self, data):
        result = []
        print("Serializando:")
        for item in data:
            result.append(
                {
                "IDArticulo":item[0],
                "IDAlmacen":0,
                "StockFisico":item[13],
                "PuntoPedido":0,
                "LoteMinimo":item[11],
                "StockSeguridad":item[9],
                "PrecioMedioA":0,
                "PrecioMedioB":0,
                "StockMedio":0,
                "Rotacion":0,
                "Inventariado":0,
                "FechaUltimoInventario":None,
                "FechaUltimoAjuste":None,
                "Predeterminado":1,
                "GestionPuntoPedido":0,
                "MarcaAuto":0,
                "FechaCreacionAudi":None,
                "FechaModificacionAudi":None,
                "UsuarioAudi":None,
                "PrecioFIFOFechaA":0,
                "PrecioFIFOFechaB":0,
                "PrecioFIFOMvtoA":0,
                "PrecioFIFOMvtoB":0,
                "FechaCalculo":None,
                "StockFechaCalculo":0,
                "IDArticuloGenerico":None,
                "FechaUltimoMovimiento":None,
                "StockFisico2":None,
                "IDUbicacion":None,
                "UsuarioCreacionAudi":None
            })
        print("End Serializer")
        return result

    @staticmethod
    def export_to_excel(name, data):
        excel = CExcel()
        columns = ['IDArticulo', 'IDAlmacen',	'StockFisico',	'PuntoPedido',	'LoteMinimo',	'StockSeguridad',	'PrecioMedioA',	'PrecioMedioB',	'StockMedio',	'Rotacion',	'Inventariado',	'FechaUltimoInventario',	'FechaUltimoAjuste',	'Predeterminado',	'GestionPuntoPedido',	'MarcaAuto','FechaCreacionAudi',	'FechaModificacionAudi',	'UsuarioAudi',	'PrecioFIFOFechaA',	'PrecioFIFOFechaB',	'PrecioFIFOMvtoA',	'PrecioFIFOMvtoB',	'FechaCalculo',	'StockFechaCalculo',	'IDArticuloGenerico',	'FechaUltimoMovimiento',	'StockFisico2',	'IDUbicacion',	'UsuarioCreacionAudi']
        excel.export_to_excel(name, data=data, columnas=columns)


# maestro_manager = MaestroArticuloAlmacenManager()
# input("Creada instancia")
# data_from_excel = maestro_manager.df_excel()
# print(len(data_from_excel))
# input("Continue...")
# data_from_industry = maestro_manager.get_data_from_industry(
#     data=data_from_excel)
# print(len(data_from_industry))
# input("Continue...")
# serialized_data = maestro_manager.serializar(data=data_from_industry)
# maestro_manager.export_to_excel(
#     name="ArticulosAlmacen.xlsx", data=serialized_data)
