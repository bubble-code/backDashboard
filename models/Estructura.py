from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from Conexion import MainConexion

Base = declarative_base()

class TbEstructura(Base):
    def __init__(self):
        self.main_conexion = MainConexion()

    __tablename__ = 'tbEstructura'

    IDEstrComp = Column(Integer, primary_key=True)
    IDTipoEstructura = Column(String(10))
    IDArticulo = Column(String(25))
    IDEstructura = Column(String(10))
    IDComponente = Column(String(25), nullable=False)
    Cantidad = Column(Numeric(23, 8), nullable=False)
    Merma = Column(Numeric(23, 8), nullable=False)
    Secuencia = Column(Integer)
    FechaCreacionAudi = Column(DateTime)
    FechaModificacionAudi = Column(DateTime)
    UsuarioAudi = Column(String(75))
    IDUdMedidaProduccion = Column(String(10))
    Factor = Column(Numeric(23, 8), nullable=False)
    CantidadProduccion = Column(Numeric(23, 8), nullable=False)
    UsuarioCreacionAudi = Column(String(75))
    Piezas = Column(Numeric(18, 2))

    def getAll(self):
        try:
            session_solmicro = self.main_conexion._open_session_solmicro()
            if session_solmicro:
                return session_solmicro.query(TbEstructura).all()
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if session_solmicro:
                session_solmicro.close()
    
    def get_column_data(self, column_name):
        try:
            session_solmicro = self.main_conexion._open_session_solmicro()
            if session_solmicro:
                # Usamos getattr para obtener el atributo de la clase TbEstructura
                column_data = session_solmicro.query(getattr(TbEstructura, column_name)).all()
                return [data[0] for data in column_data]  # Convertir a una lista los datos de la columna
        except Exception as e:
            print("Error en la consulta:", e)
        finally:
            if session_solmicro:
                session_solmicro.close()