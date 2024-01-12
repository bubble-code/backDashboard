from sqlalchemy import Column, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class MaestroCargo(Base):
    __tablename__ = 'tbMaestroCargo'

    IDCargo = Column(String(3), primary_key=True, nullable=False)
    DescCargo = Column(String(200), nullable=False)
    FechaCreacionAudi = Column(DateTime, default=func.current_timestamp())
    FechaModificacionAudi = Column(DateTime, onupdate=func.current_timestamp())
    UsuarioAudi = Column(String(75))
    IDDepartamento = Column(String(10))
    UsuarioCreacionAudi = Column(String(75))
