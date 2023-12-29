from sqlalchemy import create_engine, Column, String, Numeric, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MaestroArticuloAlmacen(Base):
    __tablename__ = 'tbMaestroArticuloAlmacen'

    IDArticulo = Column(String(25), primary_key=True)
    IDAlmacen = Column(String(10), primary_key=True)
    StockFisico = Column(Numeric(23, 8), nullable=False)
    PuntoPedido = Column(Numeric(23, 8), nullable=False)
    LoteMinimo = Column(Numeric(23, 8), nullable=False)
    StockSeguridad = Column(Numeric(23, 8), nullable=False)
    PrecioMedioA = Column(Numeric(23, 8), nullable=False)
    PrecioMedioB = Column(Numeric(23, 8), nullable=False)
    StockMedio = Column(Numeric(23, 8), nullable=False)
    Rotacion = Column(Numeric(23, 8), nullable=False)
    Inventariado = Column(Boolean, nullable=False)
    FechaUltimoInventario = Column(DateTime)
    FechaUltimoAjuste = Column(DateTime)
    Predeterminado = Column(Boolean, nullable=False)
    GestionPuntoPedido = Column(Boolean, nullable=False)
    MarcaAuto = Column(Integer, autoincrement=True, nullable=False)  
    FechaCreacionAudi = Column(DateTime)
    FechaModificacionAudi = Column(DateTime)
    UsuarioAudi = Column(String(75))
    PrecioFIFOFechaA = Column(Numeric(23, 8), nullable=False)
    PrecioFIFOFechaB = Column(Numeric(23, 8), nullable=False)
    PrecioFIFOMvtoA = Column(Numeric(23, 8), nullable=False)
    PrecioFIFOMvtoB = Column(Numeric(23, 8), nullable=False)
    FechaCalculo = Column(DateTime)
    StockFechaCalculo = Column(Numeric(23, 8), nullable=False)
    IDArticuloGenerico = Column(String(25))
    FechaUltimoMovimiento = Column(DateTime)
    StockFisico2 = Column(Numeric(23, 8), nullable=False)
    IDUbicacion = Column(String(25))
    UsuarioCreacionAudi = Column(String(75))
