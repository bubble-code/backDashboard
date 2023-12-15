from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MaestroSubfamilia(Base):
    __tablename__ = 'tbMaestroSubfamilia'

    IDTipo = Column(String(10), primary_key=True, nullable=False)
    IDFamilia = Column(String(10), nullable=False)
    IDSubfamilia = Column(String(10), nullable=False)
    DescSubfamilia = Column(String(100))
    FechaCreacionAudi = Column(DateTime)
    FechaModificacionAudi = Column(DateTime)
    UsuarioAudi = Column(String(75))
    NumCorrelativo = Column(Integer)
    Precinta = Column(Boolean, nullable=False)
    PorcMermaMaxima = Column(Numeric(23, 8))
    IDCodigo = Column(Integer)
    IDConfig = Column(String(10))
    DescConfig = Column(String(300))
    PorcRecepcionMaximo = Column(Numeric(23, 8))
    ConsejoRegulador = Column(Boolean, nullable=False)
    SeguimientoPrecinta = Column(Boolean, nullable=False)
    UsuarioCreacionAudi = Column(String(75))
