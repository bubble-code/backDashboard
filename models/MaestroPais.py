from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class MaestroPais(Base):
    __tablename__ = 'tbMaestroPais'

    IDPais = Column(String(10), primary_key=True, nullable=False)
    DescPais = Column(String(100))
    Extranjero = Column(Boolean, nullable=False)
    CEE = Column(Boolean, nullable=False)
    CanariasCeutaMelilla = Column(Boolean, nullable=False)
    FechaCreacionAudi = Column(DateTime, default=func.current_timestamp())
    FechaModificacionAudi = Column(DateTime, onupdate=func.current_timestamp())
    UsuarioAudi = Column(String(75))
    Abreviatura = Column(String(10))
    CodigoISO = Column(String(5))
    CodigoISOAlfa3 = Column(String(5))
    SEPA = Column(Boolean, nullable=False)
    IDMotivoNoAsegurado = Column(String(10))
    IdentificacionVIES = Column(String(2))
    UsuarioCreacionAudi = Column(String(75))
