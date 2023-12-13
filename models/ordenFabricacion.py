from models.Models import db
from dataclasses import dataclass


@dataclass
class OrdenFabricacion(db.Model):
    __tablename__ = 'tbOrdenFabricacion'

    IDOrden = db.Column(db.Integer, primary_key=True)
    NOrden = db.Column(db.String(25), nullable=False)
    IDContador = db.Column(db.String(10))
    IDArticulo = db.Column(db.String(25), nullable=False)
    FechaCreacion = db.Column(db.DateTime, nullable=False)
    IDCentroGestion = db.Column(db.String(10), nullable=False)
    QFabricar = db.Column(db.Numeric(23, 8), nullable=False)
    QIniciada = db.Column(db.Numeric(23, 8), nullable=False)
    QFabricada = db.Column(db.Numeric(23, 8), nullable=False)
    QRechazada = db.Column(db.Numeric(23, 8), nullable=False)
    Estado = db.Column(db.Integer, nullable=False)
    FechaInicio = db.Column(db.DateTime, nullable=False)
    FechaFin = db.Column(db.DateTime)

    def serialize(self):
        return {
            'IDOrden': self.IDOrden,
            'NOrden': self.NOrden,
            'IDContador': self.IDContador,
            'IDArticulo': self.IDArticulo,
            'FechaCreacion': self.FechaCreacion,
            'IDCentroGestion': self.IDCentroGestion,
            'QFabricar': float(self.QFabricar),  
            'QIniciada': float(self.QIniciada),
            'QFabricada': float(self.QFabricada),
            'QRechazada': float(self.QRechazada),
            'Estado': self.Estado,
            'FechaInicio': self.FechaInicio,
            'FechaFin': self.FechaFin if self.FechaFin else None
        }