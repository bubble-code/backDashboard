from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MSubfamilia(Base):
    __tablename__ = 'MSubfamilia'

    CodigoSubfamilia = Column(String(4), primary_key=True)
    Descripcion = Column(String(255))
    FechaDeAlta = Column(DateTime, default=func.current_timestamp())
    FechaUltimaModificacion = Column(DateTime, default=func.current_timestamp())
    UsuarioAlta = Column(String(50), default='Unknown')  # Assuming a default value
    UsuarioModificacion = Column(String(50), default='Unknown')  # Assuming a default value
