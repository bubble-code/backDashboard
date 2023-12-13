from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import Boolean, Column, DateTime, ForeignKeyConstraint, Index, Integer, Numeric, PrimaryKeyConstraint, UUID, Unicode, Uuid, text
from sqlalchemy.dialects.mssql import IMAGE, NTEXT
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship
from sqlalchemy.orm.base import Mapped

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class TbBdgMaestroGestionPlagas:
    __tablename__ = 'tbBdgMaestroGestionPlagas'
    __table_args__ = (
        PrimaryKeyConstraint('IDGestionPlagas', name='PK_tbBdgMaestroGestionPlagas'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDGestionPlagas: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescGestionPlagas: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbBdgMaestroGestionPlagas')})


@mapper_registry.mapped
@dataclass
class TbCRMEstadoVenta:
    __tablename__ = 'tbCRMEstadoVenta'
    __table_args__ = (
        PrimaryKeyConstraint('IDEstadoVenta', name='PK_tbCRMEstadoVenta'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDEstadoVenta: str = field(metadata={'sa': mapped_column(Unicode(2))})
    GradoAvance: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    DescEstadoVenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Grupo: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Color: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbObraEstadoPresupuesto: List[TbObraEstadoPresupuesto] = field(default_factory=list, metadata={'sa': relationship('TbObraEstadoPresupuesto', uselist=True, back_populates='tbCRMEstadoVenta')})
    tbOfertaComercialEstado: List[TbOfertaComercialEstado] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialEstado', uselist=True, back_populates='tbCRMEstadoVenta')})


@mapper_registry.mapped
@dataclass
class TbClienteBanco:
    __tablename__ = 'tbClienteBanco'
    __table_args__ = (
        ForeignKeyConstraint(['IDBanco'], ['tbMaestroBanco.IDBanco'], name='FK_tbClienteBanco_tbMaestroBanco'),
        ForeignKeyConstraint(['IDCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbClienteBanco_tbMaestroCliente'),
        PrimaryKeyConstraint('IDClienteBanco', name='PK_tbClienteBanco'),
        Index('IX_tbClienteBanco_IDBanco', 'IDBanco'),
        Index('IX_tbClienteBanco_IDCliente', 'IDCliente')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDClienteBanco: int = field(metadata={'sa': mapped_column(Integer)})
    IDCliente: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    Predeterminado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IDBanco: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Sucursal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(4))})
    DigitoControl: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    NCuenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Domicilio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    PersonaContacto: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Swift: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(11))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    CodigoIBAN: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(34))})
    ClaveGastos: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroBanco: Optional[TbMaestroBanco] = field(default=None, metadata={'sa': relationship('TbMaestroBanco', back_populates='tbClienteBanco')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbClienteBanco')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbClienteBanco')})


@mapper_registry.mapped
@dataclass
class TbClienteDireccion:
    __tablename__ = 'tbClienteDireccion'
    __table_args__ = (
        ForeignKeyConstraint(['IDAlmacen'], ['tbMaestroAlmacen.IDAlmacen'], name='FK_tbClienteDireccion_tbMaestroAlmacen'),
        ForeignKeyConstraint(['IDCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbClienteDireccion_tbMaestroCliente'),
        ForeignKeyConstraint(['IDOficinaContable'], ['tbOficinaContable.IDOficinaContable'], name='FK_tbClienteDireccion_tbOficinaContable'),
        ForeignKeyConstraint(['IDOrganoGestor'], ['tbOrganoGestor.IDOrganoGestor'], name='FK_tbClienteDireccion_tbOrganoGestor'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbClienteDireccion_tbMaestroPais'),
        ForeignKeyConstraint(['IDTipoIVA'], ['tbMaestroTipoIva.IDTipoIva'], name='FK_tbClienteDireccion_tbMaestroTipoIVA'),
        ForeignKeyConstraint(['IDUnidadTramitadora'], ['tbUnidadTramitadora.IDUnidadTramitadora'], name='FK_tbClienteDireccion_tbUnidadTramitadora'),
        PrimaryKeyConstraint('IDDireccion', name='PK_tbClienteDireccion'),
        Index('IX_tbClienteDireccion_IDCliente', 'IDCliente')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDDireccion: int = field(metadata={'sa': mapped_column(Integer)})
    IDCliente: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    Tipo: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    Predeterminada: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DireccionFactura: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Envio: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Factura: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Giro: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PredeterminadaEnvio: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PredeterminadaFactura: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PredeterminadaGiro: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DomicilioFiscal: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    EMCSDestinatario: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    EMCSLugarEntrega: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DiasTransito: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AjustarCalendario: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CodPostal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDPais: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Email: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDAlmacen: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    RazonSocial: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDConsignatario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    CifCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    EDIdestinatario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDObra: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    DuracionTransporte: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDCAE: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    CodigoTipoDestino: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    TipoDestinoInterno: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDOficinaContable: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDOrganoGestor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDUnidadTramitadora: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    EMCSAutoridadAgroalimentaria: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(30))})
    EMCSAduanaExportacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(30))})
    IDTipoIVA: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    TipoDocIdentidad: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDOrganoProponente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    AreaGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(6))})
    ContratoReferencia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(14))})
    DIRe: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(15))})
    DIR: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroAlmacen: Optional[TbMaestroAlmacen] = field(default=None, metadata={'sa': relationship('TbMaestroAlmacen', back_populates='tbClienteDireccion')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbClienteDireccion')})
    tbOficinaContable: Optional[TbOficinaContable] = field(default=None, metadata={'sa': relationship('TbOficinaContable', back_populates='tbClienteDireccion')})
    tbOrganoGestor: Optional[TbOrganoGestor] = field(default=None, metadata={'sa': relationship('TbOrganoGestor', back_populates='tbClienteDireccion')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', back_populates='tbClienteDireccion')})
    tbMaestroTipoIva: Optional[TbMaestroTipoIva] = field(default=None, metadata={'sa': relationship('TbMaestroTipoIva', back_populates='tbClienteDireccion')})
    tbUnidadTramitadora: Optional[TbUnidadTramitadora] = field(default=None, metadata={'sa': relationship('TbUnidadTramitadora', back_populates='tbClienteDireccion')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbClienteDireccion')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbClienteDireccion')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbClienteDireccion')})


@mapper_registry.mapped
@dataclass
class TbConfiguracionInforme:
    __tablename__ = 'tbConfiguracionInforme'
    __table_args__ = (
        PrimaryKeyConstraint('IDConfiguracionInforme', name='PK_tbConfiguracionInforme'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDConfiguracionInforme: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescConfiguracionInforme: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbConfiguracionInforme')})


@mapper_registry.mapped
@dataclass
class TbMaestroAgrupacion:
    __tablename__ = 'tbMaestroAgrupacion'
    __table_args__ = (
        PrimaryKeyConstraint('IDAgrupacion', name='PK_tbMaestroAgrupacion'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDAgrupacion: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescAgrupacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    DescGrupo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroTipoFactura: List[TbMaestroTipoFactura] = field(default_factory=list, metadata={'sa': relationship('TbMaestroTipoFactura', uselist=True, back_populates='tbMaestroAgrupacion')})


@mapper_registry.mapped
@dataclass
class TbMaestroAlmacen:
    __tablename__ = 'tbMaestroAlmacen'
    __table_args__ = (
        ForeignKeyConstraint(['IDCentroGestion'], ['tbMaestroCentroGestion.IDCentroGestion'], name='FK_tbMaestroAlmacen_tbMaestroCentroGestion'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroAlmacen_tbMaestroPais_IDPais'),
        PrimaryKeyConstraint('IDAlmacen', name='PK_tbMaestroAlmacen')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDAlmacen: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Deposito: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Principal: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Empresa: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    Bloqueado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Activo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    CampanaCupo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescAlmacen: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDCAE: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CodPostal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDPais: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Email: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteDireccion: List[TbClienteDireccion] = field(default_factory=list, metadata={'sa': relationship('TbClienteDireccion', uselist=True, back_populates='tbMaestroAlmacen')})
    tbMaestroCentroGestion: Optional[TbMaestroCentroGestion] = field(default=None, metadata={'sa': relationship('TbMaestroCentroGestion', back_populates='tbMaestroAlmacen')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', back_populates='tbMaestroAlmacen')})
    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroAlmacen')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroAlmacen')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroAlmacen')})


@mapper_registry.mapped
@dataclass
class TbMaestroAseguradora:
    __tablename__ = 'tbMaestroAseguradora'
    __table_args__ = (
        PrimaryKeyConstraint('IDAseguradora', name='PK_tbMaestroAseguradora'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDAseguradora: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescAseguradora: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    NumPoliza: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroAseguradora')})


@mapper_registry.mapped
@dataclass
class TbMaestroAuditor:
    __tablename__ = 'tbMaestroAuditor'
    __table_args__ = (
        PrimaryKeyConstraint('IDAuditor', name='PK_tbMaestroAuditor'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDAuditor: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Interno: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    DescAuditor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroAuditor')})


@mapper_registry.mapped
@dataclass
class TbMaestroBanco:
    __tablename__ = 'tbMaestroBanco'
    __table_args__ = (
        PrimaryKeyConstraint('IDBanco', name='PK_tbMaestroBanco'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDBanco: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescBanco: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    ImpTolerancia: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteBanco: List[TbClienteBanco] = field(default_factory=list, metadata={'sa': relationship('TbClienteBanco', uselist=True, back_populates='tbMaestroBanco')})
    tbMaestroBancoPropio: List[TbMaestroBancoPropio] = field(default_factory=list, metadata={'sa': relationship('TbMaestroBancoPropio', uselist=True, back_populates='tbMaestroBanco')})
    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroBanco')})


@mapper_registry.mapped
@dataclass
class TbMaestroBancoPropio:
    __tablename__ = 'tbMaestroBancoPropio'
    __table_args__ = (
        ForeignKeyConstraint(['IDBanco'], ['tbMaestroBanco.IDBanco'], name='FK_tbMaestroBancoPropio_tbMaestroBanco'),
        ForeignKeyConstraint(['IDMoneda'], ['tbMaestroMoneda.IDMoneda'], name='FK_IDMoneda_tbMaestroBancoPropio_tbMaestroMoneda'),
        ForeignKeyConstraint(['IDProveedor'], ['tbMaestroProveedor.IDProveedor'], name='FK_tbMaestroBancoPropio_tbMaestroProveedor'),
        ForeignKeyConstraint(['TipoConfirming'], ['tbModeloConfirming.Tipo'], name='FK_tbMaestroBancoPropio_tbModeloConfirming'),
        ForeignKeyConstraint(['TipoTrans'], ['tbModeloTransferencia.Tipo'], name='FK_tbMaestroBancoPropio_tbModeloTransferencia'),
        PrimaryKeyConstraint('IDBancoPropio', name='PK_tbMaestroBancoPropio')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDBancoPropio: str = field(metadata={'sa': mapped_column(Unicode(10))})
    InteresMinimo: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    GastoMinimo: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    GastoFijo: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    Confirming: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    SaldoSimulacion: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    Caja: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Factoring: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    PagoIntereses: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    BaseCalculo: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    CarenciaConIntereses: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IDMoneda: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    DescBancoPropio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDBanco: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Sucursal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(4))})
    DigitoControl: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    NCuenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Domicilio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    PersonaContacto: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CContable: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CEfectosDescontados: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    SufijoRemesas: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(3))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    telefono2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    TipoTrans: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(1))})
    IDClienteConfirming: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    PrefijoIBAN: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(14))})
    TipoConfirming: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(1))})
    IDCContableTalon: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Swift: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(11))})
    TipoFactoring: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(1))})
    IDClienteFactoring: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDContadorFactoring: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    NCuentaExtranjero: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    IDCContableAnticipo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CodigoIBAN: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(34))})
    TextoFactoringFacturae: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2500))})
    IDClienteConfirmingProntoPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroBanco: Optional[TbMaestroBanco] = field(default=None, metadata={'sa': relationship('TbMaestroBanco', back_populates='tbMaestroBancoPropio')})
    tbMaestroMoneda: Optional[TbMaestroMoneda] = field(default=None, metadata={'sa': relationship('TbMaestroMoneda', back_populates='tbMaestroBancoPropio')})
    tbMaestroProveedor: Optional[TbMaestroProveedor] = field(default=None, metadata={'sa': relationship('TbMaestroProveedor', foreign_keys=[IDProveedor], back_populates='tbMaestroBancoPropio')})
    tbModeloConfirming: Optional[TbModeloConfirming] = field(default=None, metadata={'sa': relationship('TbModeloConfirming', back_populates='tbMaestroBancoPropio')})
    tbModeloTransferencia: Optional[TbModeloTransferencia] = field(default=None, metadata={'sa': relationship('TbModeloTransferencia', back_populates='tbMaestroBancoPropio')})
    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroBancoPropio')})
    tbMaestroProveedor_: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, foreign_keys='[TbMaestroProveedor.IDBancoPropio]', back_populates='tbMaestroBancoPropio_')})


@mapper_registry.mapped
@dataclass
class TbMaestroCalendarioReferencia:
    __tablename__ = 'tbMaestroCalendarioReferencia'
    __table_args__ = (
        PrimaryKeyConstraint('IDCalendario', name='PK_tbMaestroCalendarioReferencia'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCalendario: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescCalendario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(150))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroCalendarioReferencia')})
    tbRHEmpresa: List[TbRHEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbRHEmpresa', uselist=True, back_populates='tbMaestroCalendarioReferencia')})


@mapper_registry.mapped
@dataclass
class TbMaestroCalificacion:
    __tablename__ = 'tbMaestroCalificacion'
    __table_args__ = (
        PrimaryKeyConstraint('IDCalificacion', name='PK_tbMaestroCalificacion'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCalificacion: str = field(metadata={'sa': mapped_column(Unicode(10))})
    FrecuenciaControl: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ControlesTrasDemerito: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    DescCalificacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, foreign_keys='[TbMaestroProveedor.IDCalificacion]', back_populates='tbMaestroCalificacion')})
    tbMaestroProveedor_: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, foreign_keys='[TbMaestroProveedor.IDCalificacionCC]', back_populates='tbMaestroCalificacion_')})


@mapper_registry.mapped
@dataclass
class TbMaestroCategoria:
    __tablename__ = 'tbMaestroCategoria'
    __table_args__ = (
        ForeignKeyConstraint(['IDEmpresa'], ['tbRHEmpresa.IDEmpresa'], name='FK_tbMaestroCategoria_tbRHEmpresa'),
        PrimaryKeyConstraint('IDCategoria', name='PK_tbMaestroCategoria')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCategoria: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescCategoria: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbRHEmpresa: Optional[TbRHEmpresa] = field(default=None, metadata={'sa': relationship('TbRHEmpresa', back_populates='tbMaestroCategoria')})
    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroCategoria')})


@mapper_registry.mapped
@dataclass
class TbMaestroCentroGestion:
    __tablename__ = 'tbMaestroCentroGestion'
    __table_args__ = (
        ForeignKeyConstraint(['IDContadorBdgOperacionPlan'], ['tbMaestroContador.IDContador'], name='FK_IDContadorBdgOperacionPlan_tbMaestroCentroGestion_tbMaestroContador'),
        ForeignKeyConstraint(['IDGrafico'], ['tbTPVGraficoRecurso.IDGrafico'], name='FK_tbMaestroCentroGestion_tbTPVGraficoRecurso'),
        ForeignKeyConstraint(['IDObraCalendario'], ['tbObraCabecera.IDObra'], name='FK_tbMaestroCentroGestion_tbObraCabecera'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroCentroGestion_tbMaestroPais'),
        ForeignKeyConstraint(['IdCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbMaestroCentroGestion_tbMaestroCliente'),
        ForeignKeyConstraint(['IdTarifa'], ['tbMaestroTarifa.IDTarifa'], name='FK_tbMaestroCentroGestion_tbMaestroTarifa'),
        PrimaryKeyConstraint('IDCentroGestion', name='PK_tbMaestroCentroGestion')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCentroGestion: str = field(metadata={'sa': mapped_column(Unicode(10))})
    SedeCentral: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GestionStock: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    SolicitOtroCentro: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ModificarSolicit: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ValidCantidad: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    PrepararExpedicion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    LanzarExpedicion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    LanzarPedidoCompra: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    LanzarOfertaCompra: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    CambiarEstado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    CambiarEstSolicit: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    FactorDimCentro: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    Propio: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CodPostal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDPais: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Email: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IdContadorPedidoVenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContadorAlbaranVenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContadorFacturaVenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContadorPedidoCompra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContadorAlbaranCompra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContadorFacturaCompra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IdTarifa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDBuzonEDI: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(36))})
    IDConsignatario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(17))})
    IDObraCalendario: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDContadorObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorCodTrabajo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorAvisos: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorObraPresup: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDBancoPropio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContadorAlbaranVentaTPV: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorVale: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDClienteIntercambio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IdContadorSolicitudTransf: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContadorRecepcionTransf: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDGrafico: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    RutaLogoTicket: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDContadorBdgOperacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorBdgOperacionPlan: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCAE: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    NIDPB: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroAlmacen: List[TbMaestroAlmacen] = field(default_factory=list, metadata={'sa': relationship('TbMaestroAlmacen', uselist=True, back_populates='tbMaestroCentroGestion')})
    tbMaestroContador: Optional[TbMaestroContador] = field(default=None, metadata={'sa': relationship('TbMaestroContador', back_populates='tbMaestroCentroGestion')})
    tbTPVGraficoRecurso: Optional[TbTPVGraficoRecurso] = field(default=None, metadata={'sa': relationship('TbTPVGraficoRecurso', back_populates='tbMaestroCentroGestion')})
    tbObraCabecera: Optional[TbObraCabecera] = field(default=None, metadata={'sa': relationship('TbObraCabecera', foreign_keys=[IDObraCalendario], back_populates='tbMaestroCentroGestion')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', back_populates='tbMaestroCentroGestion')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbMaestroCentroGestion')})
    tbMaestroTarifa: Optional[TbMaestroTarifa] = field(default=None, metadata={'sa': relationship('TbMaestroTarifa', back_populates='tbMaestroCentroGestion')})
    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroCentroGestion')})
    tbObraCabecera_: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, foreign_keys='[TbObraCabecera.IDCentroGestion]', back_populates='tbMaestroCentroGestion_')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroCentroGestion')})


@mapper_registry.mapped
@dataclass
class TbMaestroClasificacionObra:
    __tablename__ = 'tbMaestroClasificacionObra'
    __table_args__ = (
        PrimaryKeyConstraint('IDClasificacionObra', name='PK_tbMaestroClasificacionObra'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDClasificacionObra: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescClasificacionObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(500))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroClasificacionObra')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroClasificacionObra')})


@mapper_registry.mapped
@dataclass
class TbMaestroCliente:
    __tablename__ = 'tbMaestroCliente'
    __table_args__ = (
        ForeignKeyConstraint(['IDAlmacenContenedor'], ['tbMaestroAlmacen.IDAlmacen'], name='FK_tbMaestroCliente_tbMaestroAlmacen'),
        ForeignKeyConstraint(['IDAseguradora'], ['tbMaestroAseguradora.IDAseguradora'], name='FK_tbMaestroCliente_tbMaestroAseguradora'),
        ForeignKeyConstraint(['IDBancoPropio'], ['tbMaestroBancoPropio.IDBancoPropio'], name='FK_tbMaestroCliente_tbMaestroBancoPropio'),
        ForeignKeyConstraint(['IDCNAE'], ['tbMaestroCNAE.IDCNAE'], name='FK_IDCNAE_tbMaestroCliente_tbMaestroCNAE'),
        ForeignKeyConstraint(['IDClasificacionObra'], ['tbMaestroClasificacionObra.IDClasificacionObra'], name='FK_tbMaestroCliente_tbMaestroClasificacionObra'),
        ForeignKeyConstraint(['IDCondicionEnvio'], ['tbMaestroCondicionEnvio.IDCondicionEnvio'], name='FK_tbMaestroCliente_tbMaestroCondicionEnvio'),
        ForeignKeyConstraint(['IDCondicionPago'], ['tbMaestroCondicionPago.IDCondicionPago'], name='FK_tbMaestroCliente_tbMaestroCondicionPago'),
        ForeignKeyConstraint(['IDConfiguracionInforme'], ['tbConfiguracionInforme.IDConfiguracionInforme'], name='FK_tbMaestroCliente_tbConfiguracionInforme'),
        ForeignKeyConstraint(['IDDiaPago'], ['tbMaestroDiaPago.IDDiaPago'], name='FK_tbMaestroCliente_tbMaestroDiaPago'),
        ForeignKeyConstraint(['IDEmpresa'], ['tbMaestroEmpresa.IDEmpresa'], name='FK_tbMaestroCliente_tbMaestroEmpresa'),
        ForeignKeyConstraint(['IDFormaEnvio'], ['tbMaestroFormaEnvio.IDFormaEnvio'], name='FK_tbMaestroCliente_tbMaestroFormaEnvio'),
        ForeignKeyConstraint(['IDFormaPago'], ['tbMaestroFormaPago.IDFormaPago'], name='FK_tbMaestroCliente_tbMaestroFormaPago'),
        ForeignKeyConstraint(['IDGrupoCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbMaestroCliente_tbMaestroCliente'),
        ForeignKeyConstraint(['IDIdioma'], ['tbMaestroIdioma.IDIdioma'], name='FK_tbMaestroCliente_tbMaestroIdioma'),
        ForeignKeyConstraint(['IDMercado'], ['tbMaestroMercado.IDMercado'], name='FK_tbMaestroCliente_tbMaestroMercado'),
        ForeignKeyConstraint(['IDModoTransporte'], ['tbMaestroModoTrasporte.IDModoTransporte'], name='FK_tbMaestroCliente_tbMaestroModoTrasporte'),
        ForeignKeyConstraint(['IDMoneda'], ['tbMaestroMoneda.IDMoneda'], name='FK_tbMaestroCliente_tbMaestroMoneda'),
        ForeignKeyConstraint(['IDOperario'], ['tbMaestroOperario.IDOperario'], name='FK_tbMaestroCliente_tbMaestroOperario'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroCliente_tbMaestroPais'),
        ForeignKeyConstraint(['IDProveedorAsociado'], ['tbMaestroProveedor.IDProveedor'], name='FK_tbMaestroCliente_tbMaestroProveedor'),
        ForeignKeyConstraint(['IDTarifaAbono'], ['tbMaestroTarifa.IDTarifa'], name='FK_IDTarifaAbono_tbMaestroCliente_tbMaestroTarifa'),
        ForeignKeyConstraint(['IDTipoCliente'], ['tbMaestroTipoCliente.IDTipoCliente'], name='FK_tbMaestroCliente_tbMaestroTipoCliente'),
        ForeignKeyConstraint(['IDTipoEtiquetaCaja'], ['tbMaestroTipoEtiqueta.IDTipoEtiqueta'], name='FK_tbMaestroCliente_tbMaestroTipoEtiqueta1'),
        ForeignKeyConstraint(['IDTipoEtiquetaContenedor'], ['tbMaestroTipoEtiqueta.IDTipoEtiqueta'], name='FK_tbMaestroCliente_tbMaestroTipoEtiqueta'),
        ForeignKeyConstraint(['IDTipoIva'], ['tbMaestroTipoIva.IDTipoIva'], name='FK_tbMaestroCliente_tbMaestroTipoIva'),
        ForeignKeyConstraint(['IDUDExpedicion'], ['tbMaestroUdMedida.IDUdMedida'], name='FK_tbMaestroCliente_tbMaestroUDMedida'),
        ForeignKeyConstraint(['IDZona'], ['tbMaestroZona.IDZona'], name='FK_tbMaestroCliente_tbMaestroZona'),
        PrimaryKeyConstraint('IDCliente', name='PK_tbMaestroCliente'),
        Index('IX_tbMaestroCliente_IDEmpresa', 'IDEmpresa'),
        Index('IX_tbMaestroCliente_IDGrupoCliente', 'IDGrupoCliente'),
        Index('IX_tbMaestroCliente_IDMercado', 'IDMercado'),
        Index('IX_tbMaestroCliente_IDPais', 'IDPais'),
        Index('IX_tbMaestroCliente_IDZona', 'IDZona')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCliente: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescCliente: str = field(metadata={'sa': mapped_column(Unicode(300), nullable=False)})
    CifCliente: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    CodPostal: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    IDPais: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    IDFormaPago: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    IDCondicionPago: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    IDMoneda: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    TipoFacturacion: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AgrupFactura: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    Riesgo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    RiesgoConcedido: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    DtoComercial: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    CertificadoCalidad: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    AlbaranValorado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    AgrupAlbaran: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    TieneRE: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Prioridad: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    GrupoDireccion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GrupoTarifa: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GrupoArticulo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GrupoFactura: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IDTipoAsiento: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AgrupPedido: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    NumeroCopias: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    PeriodoFacturacion: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    RetencionIRPF: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    EnvioCompleto: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    MargenAdelanto: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    MargenRetraso: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    AgrupAlbaranObra: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AgrupFacturaObra: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((2))'))})
    Bloqueado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DtoComercialLinea: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    TipoGeneracionSeguros: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    FacturarTasaResiduos: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    LimiteCapitalAsegurado: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    GenerarDaa: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GrupoPresupuesto: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    EmpresaGrupo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ClienteEventual: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    NumeroCopiasAlbaranes: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    FianzaObligatoria: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PortesEspSalidas: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PortesEspRetornos: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ClienteFactoring: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    AgrupOTObra: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    TipoDocIdentidad: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    FacturaElectronica: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AgrupOT: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    IVAReducido: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GrupoRiesgo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Activo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    RiesgoInterno: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    AgrupOferta: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    ExcluirSilicie: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ExcluirDestinoSilicie: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ImpuestoPlastico: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DiasTransito: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AjustarCalendario: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    RecepcionPedidoEDI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    AlbaranEDI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FacturaEDI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    HistoricoEDI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    RequiereRanEDI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescontarPedidosServidosEDI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    TransitoUltimoAlbaranEDI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IDContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    RazonSocial: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDZona: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDDiaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10), server_default=text('((0))'))})
    IDTipoIva: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDMercado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDFormaEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCondicionEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDModoTransporte: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    ReferenciaProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    FechaAlta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime, server_default=text('(getdate())'))})
    CCEfectosCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDBancoPropio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorCargo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorAbono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCEfectosGestionCobros: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDGrupoCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDIdioma: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Email: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Web: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDBuzonEDI: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(36))})
    IDConsignatario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    IDEDIFormato: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    VerificarEDI: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IdContCodBarras: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    DiasRetraso: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((0))'))})
    IDEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    BaseDatos: Optional[UUID] = field(default=None, metadata={'sa': mapped_column(Uuid)})
    IDAlmacenContenedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDTipoEtiquetaContenedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDTipoEtiquetaCaja: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDProveedorAsociado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    TextoBloqueo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2500))})
    IDClasificacionObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    CCAnticipo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCAE: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDAseguradora: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDTipoCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    NPolizaAseg: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    FechaRiesgo: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    CCRetencion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCFianza: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    DiaFacturacion: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDOperarioBloqueo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    DescOperarioBloqueo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(250))})
    NIFRepresentanteLegal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    DepartamentoEDI: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    SeccionEDI: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDConsignatarioPagador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(17))})
    ClienteFacturaEDI: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((1))'))})
    Telefono2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Movil: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    CondicionesEspPortes: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    IDProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDOperario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCCEfectosCartera: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCNAE: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCClientePdte: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDUDExpedicion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    RefAseguradora: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(15))})
    IDMotivoNoAsegurado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDTarifaAbono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDRGSEAA: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDConfiguracionInforme: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Certif31: Optional[bool] = field(default=None, metadata={'sa': mapped_column(Boolean)})
    IDBuzonFacturaEDI: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(36))})
    IDFabricante: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteBanco: List[TbClienteBanco] = field(default_factory=list, metadata={'sa': relationship('TbClienteBanco', uselist=True, back_populates='tbMaestroCliente')})
    tbClienteDireccion: List[TbClienteDireccion] = field(default_factory=list, metadata={'sa': relationship('TbClienteDireccion', uselist=True, back_populates='tbMaestroCliente')})
    tbMaestroCentroGestion: List[TbMaestroCentroGestion] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCentroGestion', uselist=True, back_populates='tbMaestroCliente')})
    tbMaestroAlmacen: Optional[TbMaestroAlmacen] = field(default=None, metadata={'sa': relationship('TbMaestroAlmacen', back_populates='tbMaestroCliente')})
    tbMaestroAseguradora: Optional[TbMaestroAseguradora] = field(default=None, metadata={'sa': relationship('TbMaestroAseguradora', back_populates='tbMaestroCliente')})
    tbMaestroBancoPropio: Optional[TbMaestroBancoPropio] = field(default=None, metadata={'sa': relationship('TbMaestroBancoPropio', back_populates='tbMaestroCliente')})
    tbMaestroCNAE: Optional[TbMaestroCNAE] = field(default=None, metadata={'sa': relationship('TbMaestroCNAE', back_populates='tbMaestroCliente')})
    tbMaestroClasificacionObra: Optional[TbMaestroClasificacionObra] = field(default=None, metadata={'sa': relationship('TbMaestroClasificacionObra', back_populates='tbMaestroCliente')})
    tbMaestroCondicionEnvio: Optional[TbMaestroCondicionEnvio] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionEnvio', back_populates='tbMaestroCliente')})
    tbMaestroCondicionPago: Optional[TbMaestroCondicionPago] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionPago', back_populates='tbMaestroCliente')})
    tbConfiguracionInforme: Optional[TbConfiguracionInforme] = field(default=None, metadata={'sa': relationship('TbConfiguracionInforme', back_populates='tbMaestroCliente')})
    tbMaestroDiaPago: Optional[TbMaestroDiaPago] = field(default=None, metadata={'sa': relationship('TbMaestroDiaPago', back_populates='tbMaestroCliente')})
    tbMaestroEmpresa: Optional[TbMaestroEmpresa] = field(default=None, metadata={'sa': relationship('TbMaestroEmpresa', back_populates='tbMaestroCliente')})
    tbMaestroFormaEnvio: Optional[TbMaestroFormaEnvio] = field(default=None, metadata={'sa': relationship('TbMaestroFormaEnvio', back_populates='tbMaestroCliente')})
    tbMaestroFormaPago: Optional[TbMaestroFormaPago] = field(default=None, metadata={'sa': relationship('TbMaestroFormaPago', back_populates='tbMaestroCliente')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', remote_side=[IDCliente], back_populates='tbMaestroCliente_reverse')})
    tbMaestroCliente_reverse: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, remote_side=[IDGrupoCliente], back_populates='tbMaestroCliente')})
    tbMaestroIdioma: Optional[TbMaestroIdioma] = field(default=None, metadata={'sa': relationship('TbMaestroIdioma', back_populates='tbMaestroCliente')})
    tbMaestroMercado: Optional[TbMaestroMercado] = field(default=None, metadata={'sa': relationship('TbMaestroMercado', back_populates='tbMaestroCliente')})
    tbMaestroModoTrasporte: Optional[TbMaestroModoTrasporte] = field(default=None, metadata={'sa': relationship('TbMaestroModoTrasporte', back_populates='tbMaestroCliente')})
    tbMaestroMoneda: Optional[TbMaestroMoneda] = field(default=None, metadata={'sa': relationship('TbMaestroMoneda', back_populates='tbMaestroCliente')})
    tbMaestroOperario: Optional[TbMaestroOperario] = field(default=None, metadata={'sa': relationship('TbMaestroOperario', back_populates='tbMaestroCliente')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', back_populates='tbMaestroCliente')})
    tbMaestroProveedor: Optional[TbMaestroProveedor] = field(default=None, metadata={'sa': relationship('TbMaestroProveedor', back_populates='tbMaestroCliente')})
    tbMaestroTarifa: Optional[TbMaestroTarifa] = field(default=None, metadata={'sa': relationship('TbMaestroTarifa', back_populates='tbMaestroCliente')})
    tbMaestroTipoCliente: Optional[TbMaestroTipoCliente] = field(default=None, metadata={'sa': relationship('TbMaestroTipoCliente', back_populates='tbMaestroCliente')})
    tbMaestroTipoEtiqueta: Optional[TbMaestroTipoEtiqueta] = field(default=None, metadata={'sa': relationship('TbMaestroTipoEtiqueta', foreign_keys=[IDTipoEtiquetaCaja], back_populates='tbMaestroCliente')})
    tbMaestroTipoEtiqueta_: Optional[TbMaestroTipoEtiqueta] = field(default=None, metadata={'sa': relationship('TbMaestroTipoEtiqueta', foreign_keys=[IDTipoEtiquetaContenedor], back_populates='tbMaestroCliente_')})
    tbMaestroTipoIva: Optional[TbMaestroTipoIva] = field(default=None, metadata={'sa': relationship('TbMaestroTipoIva', back_populates='tbMaestroCliente')})
    tbMaestroUdMedida: Optional[TbMaestroUdMedida] = field(default=None, metadata={'sa': relationship('TbMaestroUdMedida', back_populates='tbMaestroCliente')})
    tbMaestroZona: Optional[TbMaestroZona] = field(default=None, metadata={'sa': relationship('TbMaestroZona', back_populates='tbMaestroCliente')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroCliente')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbMaestroCliente')})
    tbRHEmpresa: List[TbRHEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbRHEmpresa', uselist=True, back_populates='tbMaestroCliente')})
    tbMaestroPersonaContacto: List[TbMaestroPersonaContacto] = field(default_factory=list, metadata={'sa': relationship('TbMaestroPersonaContacto', uselist=True, back_populates='tbMaestroCliente')})
    tbClientePersonaContacto: List[TbClientePersonaContacto] = field(default_factory=list, metadata={'sa': relationship('TbClientePersonaContacto', uselist=True, back_populates='tbMaestroCliente')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroCliente')})


@mapper_registry.mapped
@dataclass
class TbMaestroCondicionEnvio:
    __tablename__ = 'tbMaestroCondicionEnvio'
    __table_args__ = (
        PrimaryKeyConstraint('IDCondicionEnvio', name='PK_tbMaestroCondicionEnvio'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCondicionEnvio: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescCondicionEnvio: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    FactorValorEstadistico: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((100))'))})
    DeclararIntrastat: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FacturaPortes: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FacturaDespacho: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FacturaOtros: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroCondicionEnvio')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroCondicionEnvio')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroCondicionEnvio')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroCondicionEnvio')})


@mapper_registry.mapped
@dataclass
class TbMaestroDepartamento:
    __tablename__ = 'tbMaestroDepartamento'
    __table_args__ = (
        PrimaryKeyConstraint('IDDepartamento', name='PK_tbMaestroDepartamento'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDDepartamento: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescDepartamento: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroDepartamento')})
    tbMaestroCargo: List[TbMaestroCargo] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCargo', uselist=True, back_populates='tbMaestroDepartamento')})


@mapper_registry.mapped
@dataclass
class TbMaestroDiaPago:
    __tablename__ = 'tbMaestroDiaPago'
    __table_args__ = (
        PrimaryKeyConstraint('IDDiaPago', name='PK_tbMaestroDiaPago'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDDiaPago: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescDiaPago: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    Dia1: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Dia2: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Dia3: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroDiaPago')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroDiaPago')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroDiaPago')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbMaestroDiaPago')})


@mapper_registry.mapped
@dataclass
class TbMaestroEmpresa:
    __tablename__ = 'tbMaestroEmpresa'
    __table_args__ = (
        ForeignKeyConstraint(['IDCNAE'], ['tbMaestroCNAE.IDCNAE'], name='FK_tbMaestroEmpresa_tbMaestroCNAE'),
        ForeignKeyConstraint(['IDCentroGestion'], ['tbMaestroCentroGestion.IDCentroGestion'], name='FK_tbMaestroEmpresa_tbMaestroCentroGestion'),
        ForeignKeyConstraint(['IDContador'], ['tbMaestroContador.IDContador'], name='FK_tbMaestroEmpresa_tbMaestroContador'),
        ForeignKeyConstraint(['IDFacturacion'], ['tbMaestroFacturacion.IDFacturacion'], name='FK_tbMaestroEmpresa_tbMaestroFacturacion'),
        ForeignKeyConstraint(['IDGrupoEmpresa'], ['tbMaestroEmpresa.IDEmpresa'], name='FK_tbMaestroEmpresa_tbMaestroEmpresa'),
        ForeignKeyConstraint(['IDMercado'], ['tbMaestroMercado.IDMercado'], name='FK_tbMaestroEmpresa_tbMaestroMercado'),
        ForeignKeyConstraint(['IDNumEmpleado'], ['tbMaestroNumEmpleado.IDNumEmpleado'], name='FK_tbMaestroEmpresa_tbMaestroNumEmpleado'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroEmpresa_tbMaestroPais'),
        ForeignKeyConstraint(['IDSector'], ['tbMaestroSector.IDSector'], name='FK_tbMaestroEmpresa_tbMaestroSector'),
        ForeignKeyConstraint(['IDZona'], ['tbMaestroZona.IDZona'], name='FK_tbMaestroEmpresa_tbMaestroZona'),
        PrimaryKeyConstraint('IDEmpresa', name='PK_tbMaestroEmpresa')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDEmpresa: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescEmpresa: str = field(metadata={'sa': mapped_column(Unicode(300), nullable=False)})
    CapitalSocial: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    Beneficios: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    Patrimonio: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ValorActivos: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ActualizarCliente: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ListaRobinson: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CasoExito: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    TipoDocIdentidad: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    EmpresaColaboradora: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Activa: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    FechaAlta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    RazonSocial: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    CifCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CodPostal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDZona: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDPais: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Telefono1: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Telefono2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Email: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Web: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDCNAE: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaUltimaActualizacion: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    DescActividad: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDFacturacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    IDNumEmpleado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    FechaEncuesta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDGrupoEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    Movil: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDSector: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDMercado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroEmpresa')})
    tbMaestroCNAE: Optional[TbMaestroCNAE] = field(default=None, metadata={'sa': relationship('TbMaestroCNAE', back_populates='tbMaestroEmpresa')})
    tbMaestroCentroGestion: Optional[TbMaestroCentroGestion] = field(default=None, metadata={'sa': relationship('TbMaestroCentroGestion', back_populates='tbMaestroEmpresa')})
    tbMaestroContador: Optional[TbMaestroContador] = field(default=None, metadata={'sa': relationship('TbMaestroContador', back_populates='tbMaestroEmpresa')})
    tbMaestroFacturacion: Optional[TbMaestroFacturacion] = field(default=None, metadata={'sa': relationship('TbMaestroFacturacion', back_populates='tbMaestroEmpresa')})
    tbMaestroEmpresa: Optional[TbMaestroEmpresa] = field(default=None, metadata={'sa': relationship('TbMaestroEmpresa', remote_side=[IDEmpresa], back_populates='tbMaestroEmpresa_reverse')})
    tbMaestroEmpresa_reverse: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, remote_side=[IDGrupoEmpresa], back_populates='tbMaestroEmpresa')})
    tbMaestroMercado: Optional[TbMaestroMercado] = field(default=None, metadata={'sa': relationship('TbMaestroMercado', back_populates='tbMaestroEmpresa')})
    tbMaestroNumEmpleado: Optional[TbMaestroNumEmpleado] = field(default=None, metadata={'sa': relationship('TbMaestroNumEmpleado', back_populates='tbMaestroEmpresa')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', back_populates='tbMaestroEmpresa')})
    tbMaestroSector: Optional[TbMaestroSector] = field(default=None, metadata={'sa': relationship('TbMaestroSector', back_populates='tbMaestroEmpresa')})
    tbMaestroZona: Optional[TbMaestroZona] = field(default=None, metadata={'sa': relationship('TbMaestroZona', back_populates='tbMaestroEmpresa')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbMaestroEmpresa')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroEmpresa')})


@mapper_registry.mapped
@dataclass
class TbMaestroFacturacion:
    __tablename__ = 'tbMaestroFacturacion'
    __table_args__ = (
        PrimaryKeyConstraint('IDFacturacion', name='PK_tbMaestroFacturacion'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDFacturacion: str = field(metadata={'sa': mapped_column(Unicode(2))})
    QDesde: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    QHasta: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    DescFacturacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(20))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroFacturacion')})


@mapper_registry.mapped
@dataclass
class TbMaestroFormaEnvio:
    __tablename__ = 'tbMaestroFormaEnvio'
    __table_args__ = (
        PrimaryKeyConstraint('IDFormaEnvio', name='PK_tbMaestroFormaEnvio'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDFormaEnvio: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescFormaEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDPorteadorEDI: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroFormaEnvio')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroFormaEnvio')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroFormaEnvio')})


@mapper_registry.mapped
@dataclass
class TbMaestroIdioma:
    __tablename__ = 'tbMaestroIdioma'
    __table_args__ = (
        PrimaryKeyConstraint('IDIdioma', name='PK_tbMaestroIdioma'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDIdioma: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescIdioma: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    CodigoISO: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(5))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroIdioma')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroIdioma')})


@mapper_registry.mapped
@dataclass
class TbMaestroMercado:
    __tablename__ = 'tbMaestroMercado'
    __table_args__ = (
        PrimaryKeyConstraint('IDMercado', name='PK_tbMaestroMercado'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDMercado: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescMercado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroMercado')})
    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroMercado')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroMercado')})
    tbMaestroCNAE: List[TbMaestroCNAE] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCNAE', uselist=True, back_populates='tbMaestroMercado')})


@mapper_registry.mapped
@dataclass
class TbMaestroModoTrasporte:
    __tablename__ = 'tbMaestroModoTrasporte'
    __table_args__ = (
        PrimaryKeyConstraint('IDModoTransporte', name='PK_tbMaestroModoTrasporte'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDModoTransporte: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescModoTransporte: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroModoTrasporte')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroModoTrasporte')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroModoTrasporte')})


@mapper_registry.mapped
@dataclass
class TbMaestroMoneda:
    __tablename__ = 'tbMaestroMoneda'
    __table_args__ = (
        PrimaryKeyConstraint('IDMoneda', name='PK_tbMaestroMoneda'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDMoneda: str = field(metadata={'sa': mapped_column(Unicode(10))})
    CambioA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    CambioB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    Abreviatura: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    NDecimalesPrec: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    NDecimalesImp: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    CodigoISO: str = field(metadata={'sa': mapped_column(Unicode(5), nullable=False)})
    DescMoneda: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCambio: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroBancoPropio: List[TbMaestroBancoPropio] = field(default_factory=list, metadata={'sa': relationship('TbMaestroBancoPropio', uselist=True, back_populates='tbMaestroMoneda')})
    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroMoneda')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroMoneda')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroMoneda')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbMaestroMoneda')})
    tbMaestroTarifa: List[TbMaestroTarifa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroTarifa', uselist=True, back_populates='tbMaestroMoneda')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroMoneda')})


@mapper_registry.mapped
@dataclass
class TbMaestroMotivoNoAsegurado:
    __tablename__ = 'tbMaestroMotivoNoAsegurado'
    __table_args__ = (
        PrimaryKeyConstraint('IDMotivo', name='PK_tbMaestroMotivoNoAsegurado'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDMotivo: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescMotivo: str = field(metadata={'sa': mapped_column(Unicode(200), nullable=False)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCondicionPago: List[TbMaestroCondicionPago] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCondicionPago', uselist=True, back_populates='tbMaestroMotivoNoAsegurado')})
    tbMaestroFormaPago: List[TbMaestroFormaPago] = field(default_factory=list, metadata={'sa': relationship('TbMaestroFormaPago', uselist=True, back_populates='tbMaestroMotivoNoAsegurado')})
    tbMaestroPais: List[TbMaestroPais] = field(default_factory=list, metadata={'sa': relationship('TbMaestroPais', uselist=True, back_populates='tbMaestroMotivoNoAsegurado')})
    tbMaestroTipoCliente: List[TbMaestroTipoCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroTipoCliente', uselist=True, back_populates='tbMaestroMotivoNoAsegurado')})


@mapper_registry.mapped
@dataclass
class TbMaestroNumEmpleado:
    __tablename__ = 'tbMaestroNumEmpleado'
    __table_args__ = (
        PrimaryKeyConstraint('IDNumEmpleado', name='PK_tbMaestroNumEmpleado'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDNumEmpleado: str = field(metadata={'sa': mapped_column(Unicode(2))})
    QDesde: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    QHasta: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    DescNumEmpleado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(20))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroNumEmpleado')})


@mapper_registry.mapped
@dataclass
class TbMaestroOficio:
    __tablename__ = 'tbMaestroOficio'
    __table_args__ = (
        PrimaryKeyConstraint('IDOficio', name='PK_tbMaestroOficio'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDOficio: str = field(metadata={'sa': mapped_column(Unicode(10))})
    EvalRiesgo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    EvalDesempeño: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescOficio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Color: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('(16777215)'))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Materiales: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Maquinaria: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IdEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdPlantilla: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(5))})
    DescDetalle: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(255))})
    Abreviatura: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(20))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroOficio')})


@mapper_registry.mapped
@dataclass
class TbMaestroOperario:
    __tablename__ = 'tbMaestroOperario'
    __table_args__ = (
        ForeignKeyConstraint(['IDBanco'], ['tbMaestroBanco.IDBanco'], name='FK_tbMaestroOperario_tbMaestroBanco'),
        ForeignKeyConstraint(['IDCalendario'], ['tbMaestroCalendarioReferencia.IDCalendario'], name='FK_tbMaestroOperario_tbMaestroCalendarioReferencia'),
        ForeignKeyConstraint(['IDCarnet'], ['tbRHTipoCarnet.IDCarnet'], name='FK_tbMaestroOperario_tbRHTipoCarnet'),
        ForeignKeyConstraint(['IDCategoria'], ['tbMaestroCategoria.IDCategoria'], name='FK_tbMaestroOperario_tbMaestroCategoria'),
        ForeignKeyConstraint(['IDColectivo'], ['tbRHColectivo.IDColectivo'], name='FK_tbMaestroOperario_tbRHColectivo'),
        ForeignKeyConstraint(['IDContador'], ['tbMaestroContador.IDContador'], name='FK_tbMaestroOperario_tbMaestroContador'),
        ForeignKeyConstraint(['IDDepartamento'], ['tbMaestroDepartamento.IDDepartamento'], name='FK_tbMaestroOperario_tbMaestroDepartamento'),
        ForeignKeyConstraint(['IDDependeDe'], ['tbMaestroOperario.IDOperario'], name='FK_tbMaestroOperario_tbMaestroOperario'),
        ForeignKeyConstraint(['IDDiscapacidad'], ['tbRHTipoDiscapacidad.IDDiscapacidad'], name='FK_tbMaestroOperario_tbRHTipoDiscapacidad'),
        ForeignKeyConstraint(['IDEmpresa'], ['tbRHEmpresa.IDEmpresa'], name='FK_tbMaestroOperario_tbRHEmpresa'),
        ForeignKeyConstraint(['IDEstadoCivil'], ['tbRHEstadoCivil.IDEstadoCivil'], name='FK_tbMaestroOperario_tbRHEstadoCivil'),
        ForeignKeyConstraint(['IDFormaPago'], ['tbMaestroFormaPago.IDFormaPago'], name='FK_tbMaestroOperario_tbMaestroFormaPago'),
        ForeignKeyConstraint(['IDGestionPlagas'], ['tbBdgMaestroGestionPlagas.IDGestionPlagas'], name='FK_tbMaestroOperario_tbBdgMaestroGestionPlagas'),
        ForeignKeyConstraint(['IDNivelAcademico'], ['tbRHNivelAcademico.IDNivelAcademico'], name='FK_tbMaestroOperario_tbRHNivelAcademico'),
        ForeignKeyConstraint(['IDOficio'], ['tbMaestroOficio.IDOficio'], name='FK_tbMaestroOperario_tbMaestroOficio'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroOperario_tbMaestroPais'),
        ForeignKeyConstraint(['IDProveedor'], ['tbMaestroProveedor.IDProveedor'], name='FK_tbMaestroOperario_tbMaestroProveedor'),
        ForeignKeyConstraint(['IdPaisNacimiento'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroOperario_tbMaestroPais_IdPaisNacimiento'),
        ForeignKeyConstraint(['IdSituacion'], ['tbRHSituacion.IdSituacion'], name='FK_tbMaestroOperario_tbRHSituacion'),
        ForeignKeyConstraint(['IdSituacionDetalle'], ['tbRHSituacionDetalle.IdSituacionDetalle'], name='FK_tbMaestroOperario_tbRHSituacionDetalle'),
        PrimaryKeyConstraint('IDOperario', name='PK_tbMaestroOperario')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDOperario: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Externo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FacturacionObras: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    PermisoGD: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    TasaHorariaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    TasaHorariaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    EstadoMaquina: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    Programable: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ProgVisible: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    CarnetConducir: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    VehiculoPropio: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    VehiculoAdaptado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    HorasReferencia: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    HorasPendientes: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    TipoDocIdentidad: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    Vendedor: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    BonosProduccion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    BonosMantenimiento: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    BonosProyectos: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    CarneBasico: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CarneCualif: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CarneFumig: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CarnePiloto: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Asesor: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescOperario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(302))})
    FechaAlta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CodPostal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDPais: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Email: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    DNI: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDCategoria: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    HorarioInicio: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    HorarioFin: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDDepartamento: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Curriculum: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(200))})
    IDOficio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDFormaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDBanco: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Sucursal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(4))})
    DigitoControl: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    NCuenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDUsuario: Optional[UUID] = field(default=None, metadata={'sa': mapped_column(Uuid)})
    Nombre: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Apellidos: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(200))})
    FechaNacimiento: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    LugarNacimiento: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    IdPaisNacimiento: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Sexo: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDEstadoCivil: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    NHijos: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Telefono2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Telefono3: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Grado: Optional[Decimal] = field(default=None, metadata={'sa': mapped_column(Numeric(23, 8), server_default=text('((0))'))})
    DiagnosticoDiscapacidad: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    Certificado: Optional[bool] = field(default=None, metadata={'sa': mapped_column(Boolean, server_default=text('((0))'))})
    FechaCertificado: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaRenovacionCertificado: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDCarnet: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(3))})
    IDNivelAcademico: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(3))})
    IDColectivo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    IDEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDSeccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdSituacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    IdSituacionDetalle: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    PrefijoNSS: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    NSS: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(8))})
    SufijoNSS: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    IDDependeDe: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCalendario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Foto: Optional[bytes] = field(default=None, metadata={'sa': mapped_column(IMAGE)})
    PeriodoObjetivos: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDDiscapacidad: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    VendedorTPV: Optional[bool] = field(default=None, metadata={'sa': mapped_column(Boolean, server_default=text('((0))'))})
    TarjetaControl: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(13))})
    PINControl: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(4))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    IDContadorTicket: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorFactura: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CodigoIBAN: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(34))})
    SWIFT: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(11))})
    ObservacionesVacaciones: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    NumeroIncripcionROPO: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    NumeroIdentificacionAsesor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDGestionPlagas: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroOperario')})
    tbMaestroBanco: Optional[TbMaestroBanco] = field(default=None, metadata={'sa': relationship('TbMaestroBanco', back_populates='tbMaestroOperario')})
    tbMaestroCalendarioReferencia: Optional[TbMaestroCalendarioReferencia] = field(default=None, metadata={'sa': relationship('TbMaestroCalendarioReferencia', back_populates='tbMaestroOperario')})
    tbRHTipoCarnet: Optional[TbRHTipoCarnet] = field(default=None, metadata={'sa': relationship('TbRHTipoCarnet', back_populates='tbMaestroOperario')})
    tbMaestroCategoria: Optional[TbMaestroCategoria] = field(default=None, metadata={'sa': relationship('TbMaestroCategoria', back_populates='tbMaestroOperario')})
    tbRHColectivo: Optional[TbRHColectivo] = field(default=None, metadata={'sa': relationship('TbRHColectivo', back_populates='tbMaestroOperario')})
    tbMaestroContador: Optional[TbMaestroContador] = field(default=None, metadata={'sa': relationship('TbMaestroContador', back_populates='tbMaestroOperario')})
    tbMaestroDepartamento: Optional[TbMaestroDepartamento] = field(default=None, metadata={'sa': relationship('TbMaestroDepartamento', back_populates='tbMaestroOperario')})
    tbMaestroOperario: Optional[TbMaestroOperario] = field(default=None, metadata={'sa': relationship('TbMaestroOperario', remote_side=[IDOperario], back_populates='tbMaestroOperario_reverse')})
    tbMaestroOperario_reverse: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, remote_side=[IDDependeDe], back_populates='tbMaestroOperario')})
    tbRHTipoDiscapacidad: Optional[TbRHTipoDiscapacidad] = field(default=None, metadata={'sa': relationship('TbRHTipoDiscapacidad', back_populates='tbMaestroOperario')})
    tbRHEmpresa: Optional[TbRHEmpresa] = field(default=None, metadata={'sa': relationship('TbRHEmpresa', back_populates='tbMaestroOperario')})
    tbRHEstadoCivil: Optional[TbRHEstadoCivil] = field(default=None, metadata={'sa': relationship('TbRHEstadoCivil', back_populates='tbMaestroOperario')})
    tbMaestroFormaPago: Optional[TbMaestroFormaPago] = field(default=None, metadata={'sa': relationship('TbMaestroFormaPago', back_populates='tbMaestroOperario')})
    tbBdgMaestroGestionPlagas: Optional[TbBdgMaestroGestionPlagas] = field(default=None, metadata={'sa': relationship('TbBdgMaestroGestionPlagas', back_populates='tbMaestroOperario')})
    tbRHNivelAcademico: Optional[TbRHNivelAcademico] = field(default=None, metadata={'sa': relationship('TbRHNivelAcademico', back_populates='tbMaestroOperario')})
    tbMaestroOficio: Optional[TbMaestroOficio] = field(default=None, metadata={'sa': relationship('TbMaestroOficio', back_populates='tbMaestroOperario')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', foreign_keys=[IDPais], back_populates='tbMaestroOperario')})
    tbMaestroProveedor: Optional[TbMaestroProveedor] = field(default=None, metadata={'sa': relationship('TbMaestroProveedor', back_populates='tbMaestroOperario')})
    tbMaestroPais_: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', foreign_keys=[IdPaisNacimiento], back_populates='tbMaestroOperario_')})
    tbRHSituacion: Optional[TbRHSituacion] = field(default=None, metadata={'sa': relationship('TbRHSituacion', back_populates='tbMaestroOperario')})
    tbRHSituacionDetalle: Optional[TbRHSituacionDetalle] = field(default=None, metadata={'sa': relationship('TbRHSituacionDetalle', back_populates='tbMaestroOperario')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroOperario')})


@mapper_registry.mapped
@dataclass
class TbMaestroProveedor:
    __tablename__ = 'tbMaestroProveedor'
    __table_args__ = (
        ForeignKeyConstraint(['IDAlmacenProveedor'], ['tbMaestroAlmacen.IDAlmacen'], name='FK_tbMaestroProveedor_tbMaestroAlmacen'),
        ForeignKeyConstraint(['IDAuditor'], ['tbMaestroAuditor.IDAuditor'], name='FK_tbMaestroProveedor_tbMaestroAuditor'),
        ForeignKeyConstraint(['IDBancoPropio'], ['tbMaestroBancoPropio.IDBancoPropio'], name='FK_tbMaestroProveedor_tbMaestroBancoPropio'),
        ForeignKeyConstraint(['IDCNAE'], ['tbMaestroCNAE.IDCNAE'], name='FK_IDCNAE_tbMaestroProveedor_tbMaestroCNAE'),
        ForeignKeyConstraint(['IDCalificacion'], ['tbMaestroCalificacion.IDCalificacion'], name='FK_tbMaestroProveedor_tbMaestroCalificacion'),
        ForeignKeyConstraint(['IDCalificacionCC'], ['tbMaestroCalificacion.IDCalificacion'], name='FK_tbMaestroProveedor_tbMaestroCalificacion1'),
        ForeignKeyConstraint(['IDCondicionEnvio'], ['tbMaestroCondicionEnvio.IDCondicionEnvio'], name='FK_tbMaestroProveedor_tbMaestroCondicionEnvio'),
        ForeignKeyConstraint(['IDCondicionPago'], ['tbMaestroCondicionPago.IDCondicionPago'], name='FK_tbMaestroProveedor_tbMaestroCondicionPago'),
        ForeignKeyConstraint(['IDContador'], ['tbMaestroContador.IDContador'], name='FK_tbMaestroProveedor_tbMaestroContador'),
        ForeignKeyConstraint(['IDDiaPago'], ['tbMaestroDiaPago.IDDiaPago'], name='FK_tbMaestroProveedor_tbMaestroDiaPago'),
        ForeignKeyConstraint(['IDFormaEnvio'], ['tbMaestroFormaEnvio.IDFormaEnvio'], name='FK_tbMaestroProveedor_tbMaestroFormaEnvio'),
        ForeignKeyConstraint(['IDFormaPago'], ['tbMaestroFormaPago.IDFormaPago'], name='FK_tbMaestroProveedor_tbMaestroFormaPago'),
        ForeignKeyConstraint(['IDMercado'], ['tbMaestroMercado.IDMercado'], name='FK_tbMaestroProveedor_tbMaestroMercado'),
        ForeignKeyConstraint(['IDModoTransporte'], ['tbMaestroModoTrasporte.IDModoTransporte'], name='FK_tbMaestroProveedor_tbMaestroModoTrasporte'),
        ForeignKeyConstraint(['IDMoneda'], ['tbMaestroMoneda.IDMoneda'], name='FK_tbMaestroProveedor_tbMaestroMoneda'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroProveedor_tbMaestroPais'),
        ForeignKeyConstraint(['IDReferencial'], ['tbMaestroReferencial.IDReferencial'], name='FK_tbMaestroProveedor_tbMaestroReferencial'),
        ForeignKeyConstraint(['IDTipoClasif'], ['tbMaestroTipoClasif.IDTipoClasif'], name='FK_tbMaestroProveedor_tbMaestroTipoClasif'),
        ForeignKeyConstraint(['IDTipoIva'], ['tbMaestroTipoIva.IDTipoIva'], name='FK_tbMaestroProveedor_tbMaestroTipoIva'),
        ForeignKeyConstraint(['IDTipoProveedor'], ['tbMaestroTipoProveedor.IDTipoProveedor'], name='FK_tbMaestroProveedor_tbMaestroTipoProveedor'),
        ForeignKeyConstraint(['IDZona'], ['tbMaestroZona.IDZona'], name='FK_tbMaestroProveedor_tbMaestroZona'),
        ForeignKeyConstraint(['IdIdioma'], ['tbMaestroIdioma.IDIdioma'], name='FK_tbMaestroProveedor_tbMaestroIdioma'),
        PrimaryKeyConstraint('IDProveedor', name='PK_tbMaestroProveedor'),
        Index('IX_tbMaestroProveedor_IDEmpresa', 'IDEmpresa'),
        Index('IX_tbMaestroProveedor_IDMercado', 'IDMercado'),
        Index('IX_tbMaestroProveedor_IDPais', 'IDPais'),
        Index('IX_tbMaestroProveedor_IDZona', 'IDZona')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDProveedor: str = field(metadata={'sa': mapped_column(Unicode(25))})
    CifProveedor: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    CodPostal: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    IDPais: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    IDFormaPago: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    IDCondicionPago: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    IDMoneda: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    RetencionIRPF: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    IDTipoAsiento: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    DtoComercial: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    AgrupFactura: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AgrupAlbaran: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    RegimenEspecial: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Homologable: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    CalidadConcertada: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    Resultado: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ResultadoCC: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    GrupoFactura: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GrupoArticulo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CertificadoCalidad: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('(0)'))})
    PorcentajeTolCierre: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImprimirEspecificacion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    TipoFacturacion: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    EmpresaGrupo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    TipoDocIdentidad: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    IVACaja: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Activo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    AgrupOferta: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    AgrupPedidoDesdeSolicitud: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    ImpuestoPlastico: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    RazonSocial: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Telefono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDZona: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDDiaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDTipoIva: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDMercado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDFormaEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCondicionEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDBancoPropio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaAlta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime, server_default=text('(getdate())'))})
    CCProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDModoTransporte: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    EMail: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDTipoProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Web: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDAlmacenProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDReferencial: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDAuditor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaValidezHomologacion: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDCalificacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaUltimaCalificacion: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaDesdeCalificada: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaHastaCalificada: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDTipoClasif: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorCargo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDContadorAbono: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCalificacionCC: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDGrupoProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    FechaHomologacion: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    NCertificado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    BaseDatos: Optional[UUID] = field(default=None, metadata={'sa': mapped_column(Uuid)})
    CCInmovilizadoLargoPlazo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCInmovilizadoCortoPlazo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    ReferenciaCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    CCEfectos: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCRetencion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCAnticipo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCFianza: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IdIdioma: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    TipoRetencionIRPF: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    NIFRepresentanteLegal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Telefono2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Movil: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    IDCNAE: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCProveedorPdte: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroBancoPropio: List[TbMaestroBancoPropio] = field(default_factory=list, metadata={'sa': relationship('TbMaestroBancoPropio', uselist=True, foreign_keys='[TbMaestroBancoPropio.IDProveedor]', back_populates='tbMaestroProveedor')})
    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroProveedor')})
    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroProveedor')})
    tbMaestroAlmacen: Optional[TbMaestroAlmacen] = field(default=None, metadata={'sa': relationship('TbMaestroAlmacen', back_populates='tbMaestroProveedor')})
    tbMaestroAuditor: Optional[TbMaestroAuditor] = field(default=None, metadata={'sa': relationship('TbMaestroAuditor', back_populates='tbMaestroProveedor')})
    tbMaestroBancoPropio_: Optional[TbMaestroBancoPropio] = field(default=None, metadata={'sa': relationship('TbMaestroBancoPropio', foreign_keys=[IDBancoPropio], back_populates='tbMaestroProveedor_')})
    tbMaestroCNAE: Optional[TbMaestroCNAE] = field(default=None, metadata={'sa': relationship('TbMaestroCNAE', back_populates='tbMaestroProveedor')})
    tbMaestroCalificacion: Optional[TbMaestroCalificacion] = field(default=None, metadata={'sa': relationship('TbMaestroCalificacion', foreign_keys=[IDCalificacion], back_populates='tbMaestroProveedor')})
    tbMaestroCalificacion_: Optional[TbMaestroCalificacion] = field(default=None, metadata={'sa': relationship('TbMaestroCalificacion', foreign_keys=[IDCalificacionCC], back_populates='tbMaestroProveedor_')})
    tbMaestroCondicionEnvio: Optional[TbMaestroCondicionEnvio] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionEnvio', back_populates='tbMaestroProveedor')})
    tbMaestroCondicionPago: Optional[TbMaestroCondicionPago] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionPago', back_populates='tbMaestroProveedor')})
    tbMaestroContador: Optional[TbMaestroContador] = field(default=None, metadata={'sa': relationship('TbMaestroContador', back_populates='tbMaestroProveedor')})
    tbMaestroDiaPago: Optional[TbMaestroDiaPago] = field(default=None, metadata={'sa': relationship('TbMaestroDiaPago', back_populates='tbMaestroProveedor')})
    tbMaestroFormaEnvio: Optional[TbMaestroFormaEnvio] = field(default=None, metadata={'sa': relationship('TbMaestroFormaEnvio', back_populates='tbMaestroProveedor')})
    tbMaestroFormaPago: Optional[TbMaestroFormaPago] = field(default=None, metadata={'sa': relationship('TbMaestroFormaPago', back_populates='tbMaestroProveedor')})
    tbMaestroMercado: Optional[TbMaestroMercado] = field(default=None, metadata={'sa': relationship('TbMaestroMercado', back_populates='tbMaestroProveedor')})
    tbMaestroModoTrasporte: Optional[TbMaestroModoTrasporte] = field(default=None, metadata={'sa': relationship('TbMaestroModoTrasporte', back_populates='tbMaestroProveedor')})
    tbMaestroMoneda: Optional[TbMaestroMoneda] = field(default=None, metadata={'sa': relationship('TbMaestroMoneda', back_populates='tbMaestroProveedor')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', back_populates='tbMaestroProveedor')})
    tbMaestroReferencial: Optional[TbMaestroReferencial] = field(default=None, metadata={'sa': relationship('TbMaestroReferencial', back_populates='tbMaestroProveedor')})
    tbMaestroTipoClasif: Optional[TbMaestroTipoClasif] = field(default=None, metadata={'sa': relationship('TbMaestroTipoClasif', back_populates='tbMaestroProveedor')})
    tbMaestroTipoIva: Optional[TbMaestroTipoIva] = field(default=None, metadata={'sa': relationship('TbMaestroTipoIva', back_populates='tbMaestroProveedor')})
    tbMaestroTipoProveedor: Optional[TbMaestroTipoProveedor] = field(default=None, metadata={'sa': relationship('TbMaestroTipoProveedor', back_populates='tbMaestroProveedor')})
    tbMaestroZona: Optional[TbMaestroZona] = field(default=None, metadata={'sa': relationship('TbMaestroZona', back_populates='tbMaestroProveedor')})
    tbMaestroIdioma: Optional[TbMaestroIdioma] = field(default=None, metadata={'sa': relationship('TbMaestroIdioma', back_populates='tbMaestroProveedor')})


@mapper_registry.mapped
@dataclass
class TbMaestroReferencial:
    __tablename__ = 'tbMaestroReferencial'
    __table_args__ = (
        PrimaryKeyConstraint('IDReferencial', name='PK_tbMaestroReferencial'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDReferencial: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescReferencial: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroReferencial')})


@mapper_registry.mapped
@dataclass
class TbMaestroSector:
    __tablename__ = 'tbMaestroSector'
    __table_args__ = (
        PrimaryKeyConstraint('IDSector', name='PK_tbMaestroSector'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDSector: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescSector: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroSector')})
    tbMaestroCNAE: List[TbMaestroCNAE] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCNAE', uselist=True, back_populates='tbMaestroSector')})


@mapper_registry.mapped
@dataclass
class TbMaestroTarifaEstado:
    __tablename__ = 'tbMaestroTarifaEstado'
    __table_args__ = (
        PrimaryKeyConstraint('IDEstado', name='PK_tbMaestroTarifaEstado'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDEstado: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Vigente: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescEstado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroTarifa: List[TbMaestroTarifa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroTarifa', uselist=True, back_populates='tbMaestroTarifaEstado')})


@mapper_registry.mapped
@dataclass
class TbMaestroTipoComprobante:
    __tablename__ = 'tbMaestroTipoComprobante'
    __table_args__ = (
        PrimaryKeyConstraint('IDTipoComprobante', name='PK_tbMaestroTipoComprobante'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoComprobante: str = field(metadata={'sa': mapped_column(Unicode(2))})
    Sistema: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescTipoComprobante: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    ClaveOperacion: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroContador: List[TbMaestroContador] = field(default_factory=list, metadata={'sa': relationship('TbMaestroContador', uselist=True, back_populates='tbMaestroTipoComprobante')})


@mapper_registry.mapped
@dataclass
class TbMaestroTipoEtiqueta:
    __tablename__ = 'tbMaestroTipoEtiqueta'
    __table_args__ = (
        PrimaryKeyConstraint('IDTipoEtiqueta', name='PK_tbMaestroTipoEtiqueta'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoEtiqueta: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescTipoEtiqueta: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    Informe: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    PredeterminadaContenedor: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PredeterminadaCaja: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Filas: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    Columnas: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((1))'))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, foreign_keys='[TbMaestroCliente.IDTipoEtiquetaCaja]', back_populates='tbMaestroTipoEtiqueta')})
    tbMaestroCliente_: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, foreign_keys='[TbMaestroCliente.IDTipoEtiquetaContenedor]', back_populates='tbMaestroTipoEtiqueta_')})


@mapper_registry.mapped
@dataclass
class TbMaestroTipoIva:
    __tablename__ = 'tbMaestroTipoIva'
    __table_args__ = (
        PrimaryKeyConstraint('IDTipoIva', name='PK_tbMaestroTipoIva'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoIva: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Factor: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    IvaRE: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    IvaIntrastat: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    SinRepercutir: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IVASinRepercutir: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    NoDeclarar: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IGIC: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('(0)'))})
    Servicios: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    NoSujetaOtros: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    NoSujetaTAI: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Obsoleto: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescTipoIva: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CCSoportado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCRepercutido: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Tipo: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    CodigoFacturae: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((1))'))})
    TaxCode: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((3))'))})
    CausaExencion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    RegimenSilicie: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(1), server_default=text("(N'4')"))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteDireccion: List[TbClienteDireccion] = field(default_factory=list, metadata={'sa': relationship('TbClienteDireccion', uselist=True, back_populates='tbMaestroTipoIva')})
    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroTipoIva')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroTipoIva')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroTipoIva')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbMaestroTipoIva')})


@mapper_registry.mapped
@dataclass
class TbMaestroTipoProveedor:
    __tablename__ = 'tbMaestroTipoProveedor'
    __table_args__ = (
        PrimaryKeyConstraint('IDTipoProveedor', name='PK_tbMaestroTipoProveedor'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoProveedor: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescTipoProveedor: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroTipoProveedor')})


@mapper_registry.mapped
@dataclass
class TbMaestroUdMedida:
    __tablename__ = 'tbMaestroUdMedida'
    __table_args__ = (
        PrimaryKeyConstraint('IDUdMedida', name='PK_tbMaestroUdMedida'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDUdMedida: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescUdMedida: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    CodigoFacturae: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((1))'))})
    IDTipoEmbalaje: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDConfig: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    DescConfig: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    UDMedidaSilicie: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(3))})
    NDecimales: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroUdMedida')})


@mapper_registry.mapped
@dataclass
class TbMaestroZona:
    __tablename__ = 'tbMaestroZona'
    __table_args__ = (
        PrimaryKeyConstraint('IDZona', name='PK_tbMaestroZona'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDZona: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescZona: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroZona')})
    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroZona')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroZona')})


@mapper_registry.mapped
@dataclass
class TbModeloConfirming:
    __tablename__ = 'tbModeloConfirming'
    __table_args__ = (
        PrimaryKeyConstraint('Tipo', name='PK_tbModeloConfirming'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    Tipo: str = field(metadata={'sa': mapped_column(Unicode(1))})
    Descripcion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(70))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroBancoPropio: List[TbMaestroBancoPropio] = field(default_factory=list, metadata={'sa': relationship('TbMaestroBancoPropio', uselist=True, back_populates='tbModeloConfirming')})


@mapper_registry.mapped
@dataclass
class TbModeloTransferencia:
    __tablename__ = 'tbModeloTransferencia'
    __table_args__ = (
        PrimaryKeyConstraint('Tipo', name='PK_tbModeloTransferencia'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    Tipo: str = field(metadata={'sa': mapped_column(Unicode(1))})
    Descripcion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(70))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroBancoPropio: List[TbMaestroBancoPropio] = field(default_factory=list, metadata={'sa': relationship('TbMaestroBancoPropio', uselist=True, back_populates='tbModeloTransferencia')})


@mapper_registry.mapped
@dataclass
class TbObraCabecera:
    __tablename__ = 'tbObraCabecera'
    __table_args__ = (
        ForeignKeyConstraint(['IDAlmacen'], ['tbMaestroAlmacen.IDAlmacen'], name='FK_tbObraCabecera_tbMaestroAlmacen'),
        ForeignKeyConstraint(['IDCentroGestion'], ['tbMaestroCentroGestion.IDCentroGestion'], name='FK_tbObraCabecera_tbMaestroCentroGestion'),
        ForeignKeyConstraint(['IDClasificacionObra'], ['tbMaestroClasificacionObra.IDClasificacionObra'], name='FK_tbObraCabecera_tbMaestroClasificacionObra'),
        ForeignKeyConstraint(['IDCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbObraCabecera_tbMaestroCliente'),
        ForeignKeyConstraint(['IDClienteBanco'], ['tbClienteBanco.IDClienteBanco'], name='FK_tbObraCabecera_tbClienteBanco'),
        ForeignKeyConstraint(['IDCondicionEnvio'], ['tbMaestroCondicionEnvio.IDCondicionEnvio'], name='FK_tbObraCabecera_tbMaestroCondicionEnvio'),
        ForeignKeyConstraint(['IDCondicionPago'], ['tbMaestroCondicionPago.IDCondicionPago'], name='FK_tbObraCabecera_tbMaestroCondicionPago'),
        ForeignKeyConstraint(['IDDiaPago'], ['tbMaestroDiaPago.IDDiaPago'], name='FK_tbObraCabecera_tbMaestroDiaPago'),
        ForeignKeyConstraint(['IDDireccionFra'], ['tbClienteDireccion.IDDireccion'], name='FK_tbObraCabecera_tbClienteDireccion'),
        ForeignKeyConstraint(['IDFormaPago'], ['tbMaestroFormaPago.IDFormaPago'], name='FK_tbObraCabecera_tbMaestroFormaPago'),
        ForeignKeyConstraint(['IDMoneda'], ['tbMaestroMoneda.IDMoneda'], name='FK_tbObraCabecera_tbMaestroMoneda'),
        ForeignKeyConstraint(['IDObraPadre'], ['tbObraCabecera.IDObra'], name='FK_tbObraCabecera_tbObraCabecera'),
        ForeignKeyConstraint(['IDPresup'], ['tbObraPresupCabecera.IDPresup'], name='FK_tbObraCabecera_tbObraPresupCabecera'),
        ForeignKeyConstraint(['IDTipoIva'], ['tbMaestroTipoIva.IDTipoIva'], name='FK_tbObraCabecera_tbMaestroTipoIva'),
        ForeignKeyConstraint(['IDTipoObra'], ['tbObraTipo.IDTipoObra'], name='FK_tbObraCabecera_tbObraTipo'),
        PrimaryKeyConstraint('IDObra', name='PK_tbObraCabecera'),
        Index('IX_tbObraCabecera_Estado', 'Estado'),
        Index('IX_tbObraCabecera_IDCliente', 'IDCliente'),
        Index('IX_tbObraCabecera_IDObraOrigen', 'IDObraOrigen'),
        Index('IX_tbObraCabecera_NObra', 'NObra')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDObra: int = field(metadata={'sa': mapped_column(Integer)})
    CambioA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    CambioB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    Estado: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    ImpPrevA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPrevB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    MargenPrevTrabajo: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPrevVentaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPrevVentaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    MargenRealTrabajo: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpRealA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpRealB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpFactA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpFactB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPrevA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPrevB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPrevVentaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPrevVentaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQRealA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQRealB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQFactA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQFactB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    TipoMnto: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    FacturarDiasMinimos: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    AlbaranValorado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ObraPedClteAbierto: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FacturarPlusPorContadores: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    NoFacturaPortes: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ClienteGenerico: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FacturarTasaResiduos: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    NObra: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    Retencion: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    IDClase: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('(0)'))})
    PortesEspSalidas: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PortesEspRetornos: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ImprimibleCondPortes: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    GastosGenerales: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    BeneficioIndustrial: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    CoefBaja: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    TipoCertificacion: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    SeguroCambio: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IDContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    DescObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDTipoObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaObra: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaInicio: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaFin: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDMoneda: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDDireccion: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    NumeroSalida: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDPresup: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    NumeroPedido: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDFormaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCondicionPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDObraOrigen: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CodPostal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CCPrestamoHip: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CCAnticipo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    URLContratoTipo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    CCCompCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDAlmacen: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    PathContrato: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDCondicionEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDClienteBanco: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDDiaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDObraPadre: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    TipoGeneracionSeguros: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((0))'))})
    IDCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    PedidoClienteAbierto: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    DiaFacturacion: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Nivel: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDClasificacionObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDObraCalendario: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    UrlIRPFTipo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    PathIRPF: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    TipoRetencion: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaRetencion: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDTipoIva: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Periodo: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    TipoPeriodo: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Impuestos: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDActivo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDDireccionFra: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCosteKgUva: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    Vendimia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    KgsEntradaUva: Optional[Decimal] = field(default=None, metadata={'sa': mapped_column(Numeric(23, 8))})
    CosteKgUva: Optional[Decimal] = field(default=None, metadata={'sa': mapped_column(Numeric(23, 8))})
    CondicionesEspPortes: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCentroGestion: List[TbMaestroCentroGestion] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCentroGestion', uselist=True, foreign_keys='[TbMaestroCentroGestion.IDObraCalendario]', back_populates='tbObraCabecera')})
    tbMaestroAlmacen: Optional[TbMaestroAlmacen] = field(default=None, metadata={'sa': relationship('TbMaestroAlmacen', back_populates='tbObraCabecera')})
    tbMaestroCentroGestion_: Optional[TbMaestroCentroGestion] = field(default=None, metadata={'sa': relationship('TbMaestroCentroGestion', foreign_keys=[IDCentroGestion], back_populates='tbObraCabecera_')})
    tbMaestroClasificacionObra: Optional[TbMaestroClasificacionObra] = field(default=None, metadata={'sa': relationship('TbMaestroClasificacionObra', back_populates='tbObraCabecera')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbObraCabecera')})
    tbClienteBanco: Optional[TbClienteBanco] = field(default=None, metadata={'sa': relationship('TbClienteBanco', back_populates='tbObraCabecera')})
    tbMaestroCondicionEnvio: Optional[TbMaestroCondicionEnvio] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionEnvio', back_populates='tbObraCabecera')})
    tbMaestroCondicionPago: Optional[TbMaestroCondicionPago] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionPago', back_populates='tbObraCabecera')})
    tbMaestroDiaPago: Optional[TbMaestroDiaPago] = field(default=None, metadata={'sa': relationship('TbMaestroDiaPago', back_populates='tbObraCabecera')})
    tbClienteDireccion: Optional[TbClienteDireccion] = field(default=None, metadata={'sa': relationship('TbClienteDireccion', back_populates='tbObraCabecera')})
    tbMaestroFormaPago: Optional[TbMaestroFormaPago] = field(default=None, metadata={'sa': relationship('TbMaestroFormaPago', back_populates='tbObraCabecera')})
    tbMaestroMoneda: Optional[TbMaestroMoneda] = field(default=None, metadata={'sa': relationship('TbMaestroMoneda', back_populates='tbObraCabecera')})
    tbObraCabecera: Optional[TbObraCabecera] = field(default=None, metadata={'sa': relationship('TbObraCabecera', remote_side=[IDObra], back_populates='tbObraCabecera_reverse')})
    tbObraCabecera_reverse: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, remote_side=[IDObraPadre], back_populates='tbObraCabecera')})
    tbObraPresupCabecera: Optional[TbObraPresupCabecera] = field(default=None, metadata={'sa': relationship('TbObraPresupCabecera', back_populates='tbObraCabecera')})
    tbMaestroTipoIva: Optional[TbMaestroTipoIva] = field(default=None, metadata={'sa': relationship('TbMaestroTipoIva', back_populates='tbObraCabecera')})
    tbObraTipo: Optional[TbObraTipo] = field(default=None, metadata={'sa': relationship('TbObraTipo', foreign_keys=[IDTipoObra], back_populates='tbObraCabecera')})
    tbObraTipo_: List[TbObraTipo] = field(default_factory=list, metadata={'sa': relationship('TbObraTipo', uselist=True, foreign_keys='[TbObraTipo.IDObraModelo]', back_populates='tbObraCabecera_')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbObraCabecera')})


@mapper_registry.mapped
@dataclass
class TbObraPresupCabecera:
    __tablename__ = 'tbObraPresupCabecera'
    __table_args__ = (
        ForeignKeyConstraint(['Estado'], ['tbObraEstadoPresupuesto.IDEstado'], name='FK_tbObraPresupCabecera_tbObraEstadoPresupuesto'),
        ForeignKeyConstraint(['IDCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbObraPresupCabecera_tbMaestroCliente'),
        ForeignKeyConstraint(['IDCondicionPago'], ['tbMaestroCondicionPago.IDCondicionPago'], name='FK_tbObraPresupCabecera_tbMaestroCondicionPago'),
        ForeignKeyConstraint(['IDDiaPago'], ['tbMaestroDiaPago.IDDiaPago'], name='FK_tbObraPresupCabecera_tbMaestroDiaPago'),
        ForeignKeyConstraint(['IDDireccion'], ['tbClienteDireccion.IDDireccion'], name='FK_tbObraPresupCabecera_tbClienteDireccion'),
        ForeignKeyConstraint(['IDEmpresa'], ['tbMaestroEmpresa.IDEmpresa'], name='FK_tbObraPresupCabecera_tbMaestroEmpresa'),
        ForeignKeyConstraint(['IDFormaPago'], ['tbMaestroFormaPago.IDFormaPago'], name='FK_tbObraPresupCabecera_tbMaestroFormaPago'),
        ForeignKeyConstraint(['IDMoneda'], ['tbMaestroMoneda.IDMoneda'], name='FK_tbObraPresupCabecera_tbMaestroMoneda'),
        ForeignKeyConstraint(['IDTipoIva'], ['tbMaestroTipoIva.IDTipoIva'], name='FK_tbObraPresupCabecera_tbMaestroTipoIva'),
        ForeignKeyConstraint(['IDTipoObra'], ['tbObraTipo.IDTipoObra'], name='FK_tbObraPresupCabecera_tbObraTipo'),
        PrimaryKeyConstraint('IDPresup', name='PK_tbObraPresupCabecera'),
        Index('IX_tbObraPresupCabecera', 'NumPresup', 'RevPresup')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDPresup: int = field(metadata={'sa': mapped_column(Integer)})
    NumPresup: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    RevPresup: int = field(metadata={'sa': mapped_column(Integer, nullable=False)})
    CambioA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    CambioB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    MargenPresupTrabajo: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupVentaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupVentaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPresupA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPresupB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPresupVentaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpQPresupVentaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupQTrabajoA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupQTrabajoB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupQTrabajoVentaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpPresupQTrabajoVentaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    GastosGenerales: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    BeneficioIndustrial: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    CoefBaja: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    TipoMnto: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    IDContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    DescPresup: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDTipoObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaPresup: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDMoneda: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDDireccion: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Estado: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDObra: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaPeticion: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaEmision: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaCierre: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaValidez: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    URLPresupuesto: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    NumeroPedido: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDFormaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCondicionPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDDiaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDTipoIva: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDResponsable: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDClasificacionObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    IDResponsableComer: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbObraPresupCabecera')})
    tbObraEstadoPresupuesto: Optional[TbObraEstadoPresupuesto] = field(default=None, metadata={'sa': relationship('TbObraEstadoPresupuesto', back_populates='tbObraPresupCabecera')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbObraPresupCabecera')})
    tbMaestroCondicionPago: Optional[TbMaestroCondicionPago] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionPago', back_populates='tbObraPresupCabecera')})
    tbMaestroDiaPago: Optional[TbMaestroDiaPago] = field(default=None, metadata={'sa': relationship('TbMaestroDiaPago', back_populates='tbObraPresupCabecera')})
    tbClienteDireccion: Optional[TbClienteDireccion] = field(default=None, metadata={'sa': relationship('TbClienteDireccion', back_populates='tbObraPresupCabecera')})
    tbMaestroEmpresa: Optional[TbMaestroEmpresa] = field(default=None, metadata={'sa': relationship('TbMaestroEmpresa', back_populates='tbObraPresupCabecera')})
    tbMaestroFormaPago: Optional[TbMaestroFormaPago] = field(default=None, metadata={'sa': relationship('TbMaestroFormaPago', back_populates='tbObraPresupCabecera')})
    tbMaestroMoneda: Optional[TbMaestroMoneda] = field(default=None, metadata={'sa': relationship('TbMaestroMoneda', back_populates='tbObraPresupCabecera')})
    tbMaestroTipoIva: Optional[TbMaestroTipoIva] = field(default=None, metadata={'sa': relationship('TbMaestroTipoIva', back_populates='tbObraPresupCabecera')})
    tbObraTipo: Optional[TbObraTipo] = field(default=None, metadata={'sa': relationship('TbObraTipo', back_populates='tbObraPresupCabecera')})


@mapper_registry.mapped
@dataclass
class TbObraTipo:
    __tablename__ = 'tbObraTipo'
    __table_args__ = (
        ForeignKeyConstraint(['IDObraModelo'], ['tbObraCabecera.IDObra'], name='FK_tbObraTipo_tbObraCabecera_IDObraModelo'),
        PrimaryKeyConstraint('IDTipoObra', name='PK_tbObraTipo')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoObra: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Externa: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Interna: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescTipoObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(1000))})
    Tipo: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDObraModelo: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, foreign_keys='[TbObraCabecera.IDTipoObra]', back_populates='tbObraTipo')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbObraTipo')})
    tbObraCabecera_: Optional[TbObraCabecera] = field(default=None, metadata={'sa': relationship('TbObraCabecera', foreign_keys=[IDObraModelo], back_populates='tbObraTipo_')})


@mapper_registry.mapped
@dataclass
class TbOfertaComercialTipo:
    __tablename__ = 'tbOfertaComercialTipo'
    __table_args__ = (
        PrimaryKeyConstraint('IDTipoOfertaComercial', name='PK_tbOfertaComercialTipo'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoOfertaComercial: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescTipoOferta: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    ActualizarCliente: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    LanzarCompra: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    LanzarVenta: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDTipoObra: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbOfertaComercialTipo')})


@mapper_registry.mapped
@dataclass
class TbOficinaContable:
    __tablename__ = 'tbOficinaContable'
    __table_args__ = (
        PrimaryKeyConstraint('IDOficinaContable', name='PK_tbOficinaContable'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDOficinaContable: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescOficinaContable: str = field(metadata={'sa': mapped_column(Unicode(200), nullable=False)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Nombre: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    Apellido1: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    Apellido2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    DireccionEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(80))})
    CPEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(5))})
    CiudadEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    ProvinciaEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(20))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteDireccion: List[TbClienteDireccion] = field(default_factory=list, metadata={'sa': relationship('TbClienteDireccion', uselist=True, back_populates='tbOficinaContable')})


@mapper_registry.mapped
@dataclass
class TbOrganoGestor:
    __tablename__ = 'tbOrganoGestor'
    __table_args__ = (
        PrimaryKeyConstraint('IDOrganoGestor', name='PK_tbOrganoGestor'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDOrganoGestor: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescOrganoGestor: str = field(metadata={'sa': mapped_column(Unicode(200), nullable=False)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Nombre: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    Apellido1: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    Apellido2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    DireccionEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(80))})
    CPEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(5))})
    CiudadEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    ProvinciaEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(20))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteDireccion: List[TbClienteDireccion] = field(default_factory=list, metadata={'sa': relationship('TbClienteDireccion', uselist=True, back_populates='tbOrganoGestor')})


@mapper_registry.mapped
@dataclass
class TbRHColectivo:
    __tablename__ = 'tbRHColectivo'
    __table_args__ = (
        PrimaryKeyConstraint('IDColectivo', name='PK_tbRHColectivo'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDColectivo: str = field(metadata={'sa': mapped_column(Unicode(2))})
    DescColectivo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHColectivo')})


@mapper_registry.mapped
@dataclass
class TbRHEmpresa:
    __tablename__ = 'tbRHEmpresa'
    __table_args__ = (
        ForeignKeyConstraint(['IDCalendario'], ['tbMaestroCalendarioReferencia.IDCalendario'], name='FK_tbRHEmpresa_tbMaestroCalendarioReferencia'),
        ForeignKeyConstraint(['IDClienteEnvioCentralizado'], ['tbMaestroCliente.IDCliente'], name='FK_IDClienteEnvioCentralizado_tbRHEmpresa_tbMaestroCliente'),
        PrimaryKeyConstraint('IDEmpresa', name='PK_tbRHEmpresa')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDEmpresa: str = field(metadata={'sa': mapped_column(Unicode(10))})
    CuadroTripartito: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Prevencion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    PredeterminadaBaja: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    EmpresaMatriz: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDCalendario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    EmpresaPadre: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDConfig: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    DescConfig: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDClienteEnvioCentralizado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCategoria: List[TbMaestroCategoria] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCategoria', uselist=True, back_populates='tbRHEmpresa')})
    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHEmpresa')})
    tbMaestroCalendarioReferencia: Optional[TbMaestroCalendarioReferencia] = field(default=None, metadata={'sa': relationship('TbMaestroCalendarioReferencia', back_populates='tbRHEmpresa')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbRHEmpresa')})


@mapper_registry.mapped
@dataclass
class TbRHEstadoCivil:
    __tablename__ = 'tbRHEstadoCivil'
    __table_args__ = (
        PrimaryKeyConstraint('IDEstadoCivil', name='PK_tbRHEstadoCivil'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDEstadoCivil: str = field(metadata={'sa': mapped_column(Unicode(2))})
    DescEstadoCivil: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHEstadoCivil')})


@mapper_registry.mapped
@dataclass
class TbRHNivelAcademico:
    __tablename__ = 'tbRHNivelAcademico'
    __table_args__ = (
        PrimaryKeyConstraint('IDNivelAcademico', name='PK_tbRHNivelAcademico'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDNivelAcademico: str = field(metadata={'sa': mapped_column(Unicode(3))})
    DescNivelAcademico: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHNivelAcademico')})


@mapper_registry.mapped
@dataclass
class TbRHSituacion:
    __tablename__ = 'tbRHSituacion'
    __table_args__ = (
        PrimaryKeyConstraint('IdSituacion', name='PK_tbRHSituacion'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IdSituacion: str = field(metadata={'sa': mapped_column(Unicode(2))})
    Predeterminado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescSituacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    Estado: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Candidato: Optional[bool] = field(default=None, metadata={'sa': mapped_column(Boolean, server_default=text('((1))'))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHSituacion')})


@mapper_registry.mapped
@dataclass
class TbRHSituacionDetalle:
    __tablename__ = 'tbRHSituacionDetalle'
    __table_args__ = (
        PrimaryKeyConstraint('IdSituacionDetalle', name='PK_tbRHSituacionDetalle'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IdSituacionDetalle: str = field(metadata={'sa': mapped_column(Unicode(2))})
    Predeterminado: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescSituacionDetalle: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    Estado: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHSituacionDetalle')})


@mapper_registry.mapped
@dataclass
class TbRHTipoCarnet:
    __tablename__ = 'tbRHTipoCarnet'
    __table_args__ = (
        PrimaryKeyConstraint('IDCarnet', name='PK_tbRHTipoCarnet'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCarnet: str = field(metadata={'sa': mapped_column(Unicode(3))})
    DescCarnet: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHTipoCarnet')})


@mapper_registry.mapped
@dataclass
class TbRHTipoDiscapacidad:
    __tablename__ = 'tbRHTipoDiscapacidad'
    __table_args__ = (
        PrimaryKeyConstraint('IDDiscapacidad', name='PK_tbRHTipoDiscapacidad'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDDiscapacidad: str = field(metadata={'sa': mapped_column(Unicode(2))})
    Estadistica: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescDiscapacidad: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbRHTipoDiscapacidad')})


@mapper_registry.mapped
@dataclass
class TbTPVGraficoRecurso:
    __tablename__ = 'tbTPVGraficoRecurso'
    __table_args__ = (
        PrimaryKeyConstraint('IDGrafico', name='PK_tbTPVGraficoRecurso'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDGrafico: int = field(metadata={'sa': mapped_column(Integer)})
    DescGrafico: str = field(metadata={'sa': mapped_column(Unicode(300), nullable=False)})
    GraficoXML: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCentroGestion: List[TbMaestroCentroGestion] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCentroGestion', uselist=True, back_populates='tbTPVGraficoRecurso')})


@mapper_registry.mapped
@dataclass
class TbUnidadTramitadora:
    __tablename__ = 'tbUnidadTramitadora'
    __table_args__ = (
        PrimaryKeyConstraint('IDUnidadTramitadora', name='PK_tbUnidadTramitadora'),
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDUnidadTramitadora: str = field(metadata={'sa': mapped_column(Unicode(25))})
    DescUnidadTramitadora: str = field(metadata={'sa': mapped_column(Unicode(200), nullable=False)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Nombre: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    Apellido1: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    Apellido2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(40))})
    DireccionEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(80))})
    CPEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(5))})
    CiudadEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    ProvinciaEspana: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(20))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteDireccion: List[TbClienteDireccion] = field(default_factory=list, metadata={'sa': relationship('TbClienteDireccion', uselist=True, back_populates='tbUnidadTramitadora')})


@mapper_registry.mapped
@dataclass
class TbMaestroCNAE:
    __tablename__ = 'tbMaestroCNAE'
    __table_args__ = (
        ForeignKeyConstraint(['IDMercado'], ['tbMaestroMercado.IDMercado'], name='FK_tbMaestroCNAE_tbMaestroMercado'),
        ForeignKeyConstraint(['IDSector'], ['tbMaestroSector.IDSector'], name='FK_tbMaestroCNAE_tbMaestroSector'),
        PrimaryKeyConstraint('IDCNAE', name='PK_tbMaestroCNAE')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCNAE: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescCNAE: str = field(metadata={'sa': mapped_column(Unicode(300), nullable=False)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDSector: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDMercado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroCNAE')})
    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroCNAE')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroCNAE')})
    tbMaestroMercado: Optional[TbMaestroMercado] = field(default=None, metadata={'sa': relationship('TbMaestroMercado', back_populates='tbMaestroCNAE')})
    tbMaestroSector: Optional[TbMaestroSector] = field(default=None, metadata={'sa': relationship('TbMaestroSector', back_populates='tbMaestroCNAE')})


@mapper_registry.mapped
@dataclass
class TbMaestroCargo:
    __tablename__ = 'tbMaestroCargo'
    __table_args__ = (
        ForeignKeyConstraint(['IDDepartamento'], ['tbMaestroDepartamento.IDDepartamento'], name='FK_tbMaestroCargo_tbMaestroDepartamento_IDDepartamento'),
        PrimaryKeyConstraint('IDCargo', name='PK_tbMaestroCargo')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCargo: str = field(metadata={'sa': mapped_column(Unicode(3))})
    DescCargo: str = field(metadata={'sa': mapped_column(Unicode(200), nullable=False)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDDepartamento: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroDepartamento: Optional[TbMaestroDepartamento] = field(default=None, metadata={'sa': relationship('TbMaestroDepartamento', back_populates='tbMaestroCargo')})
    tbMaestroPersonaContacto: List[TbMaestroPersonaContacto] = field(default_factory=list, metadata={'sa': relationship('TbMaestroPersonaContacto', uselist=True, back_populates='tbMaestroCargo')})
    tbClientePersonaContacto: List[TbClientePersonaContacto] = field(default_factory=list, metadata={'sa': relationship('TbClientePersonaContacto', uselist=True, back_populates='tbMaestroCargo')})


@mapper_registry.mapped
@dataclass
class TbMaestroCondicionPago:
    __tablename__ = 'tbMaestroCondicionPago'
    __table_args__ = (
        ForeignKeyConstraint(['IDMotivoNoAsegurado'], ['tbMaestroMotivoNoAsegurado.IDMotivo'], name='FK_IDMotivoNoAsegurado_tbMaestroCondicionPago_tbMaestroMotivoNoAsegurado'),
        PrimaryKeyConstraint('IDCondicionPago', name='PK_tbMaestroCondicionPago')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDCondicionPago: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescCondicionPago: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    DtoProntoPago: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    RecFinan: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDMotivoNoAsegurado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroCondicionPago')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroCondicionPago')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroCondicionPago')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbMaestroCondicionPago')})
    tbMaestroMotivoNoAsegurado: Optional[TbMaestroMotivoNoAsegurado] = field(default=None, metadata={'sa': relationship('TbMaestroMotivoNoAsegurado', back_populates='tbMaestroCondicionPago')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroCondicionPago')})


@mapper_registry.mapped
@dataclass
class TbMaestroContador:
    __tablename__ = 'tbMaestroContador'
    __table_args__ = (
        ForeignKeyConstraint(['IDTipoComprobante'], ['tbMaestroTipoComprobante.IDTipoComprobante'], name='FK_tbMaestroContador_tbMaestroTipoComprobante'),
        PrimaryKeyConstraint('IDContador', name='PK_tbMaestroContador')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDContador: str = field(metadata={'sa': mapped_column(Unicode(10))})
    DescContador: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    Contador: int = field(metadata={'sa': mapped_column(Integer, nullable=False)})
    Longitud: int = field(metadata={'sa': mapped_column(Integer, nullable=False)})
    Numerico: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ContadorIni: int = field(metadata={'sa': mapped_column(Integer, nullable=False)})
    AIva: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    DiferenteFacturacion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    EmitidaPorTerceros: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ConcatenarContador: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    Formato: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    ContadorFin: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDTipoComprobante: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCentroGestion: List[TbMaestroCentroGestion] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCentroGestion', uselist=True, back_populates='tbMaestroContador')})
    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroContador')})
    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroContador')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroContador')})
    tbMaestroTipoComprobante: Optional[TbMaestroTipoComprobante] = field(default=None, metadata={'sa': relationship('TbMaestroTipoComprobante', back_populates='tbMaestroContador')})


@mapper_registry.mapped
@dataclass
class TbMaestroFormaPago:
    __tablename__ = 'tbMaestroFormaPago'
    __table_args__ = (
        ForeignKeyConstraint(['IDMotivoNoAsegurado'], ['tbMaestroMotivoNoAsegurado.IDMotivo'], name='FK_IDMotivoNoAsegurado_tbMaestroFormaPago_tbMaestroMotivoNoAsegurado'),
        PrimaryKeyConstraint('IDFormaPago', name='PK_tbMaestroFormaPago')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDFormaPago: str = field(metadata={'sa': mapped_column(Unicode(10))})
    CobroRemesable: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CobroImprimible: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CobroALaVista: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ChequeTalon: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Trasferencia: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ContabilidadEnVto: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DiasMargenRiesgo: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    Factoring: int = field(metadata={'sa': mapped_column(Integer, nullable=False, server_default=text('((0))'))})
    Tarjeta: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Efectivo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Vale: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescFormaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    CondicionVentaFactoring: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CodigoFacturae: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((1))'))})
    IDMotivoNoAsegurado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroFormaPago')})
    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, back_populates='tbMaestroFormaPago')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroFormaPago')})
    tbObraCabecera: List[TbObraCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraCabecera', uselist=True, back_populates='tbMaestroFormaPago')})
    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbMaestroFormaPago')})
    tbMaestroMotivoNoAsegurado: Optional[TbMaestroMotivoNoAsegurado] = field(default=None, metadata={'sa': relationship('TbMaestroMotivoNoAsegurado', back_populates='tbMaestroFormaPago')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbMaestroFormaPago')})


@mapper_registry.mapped
@dataclass
class TbMaestroPais:
    __tablename__ = 'tbMaestroPais'
    __table_args__ = (
        ForeignKeyConstraint(['IDMotivoNoAsegurado'], ['tbMaestroMotivoNoAsegurado.IDMotivo'], name='FK_IDMotivoNoAsegurado_tbMaestroPais_tbMaestroMotivoNoAsegurado'),
        PrimaryKeyConstraint('IDPais', name='PK_tbMaestroPais')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDPais: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Extranjero: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CEE: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    CanariasCeutaMelilla: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    SEPA: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescPais: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Abreviatura: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    CodigoISO: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(5))})
    CodigoISOAlfa3: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(5))})
    IDMotivoNoAsegurado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdentificacionVIES: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbClienteDireccion: List[TbClienteDireccion] = field(default_factory=list, metadata={'sa': relationship('TbClienteDireccion', uselist=True, back_populates='tbMaestroPais')})
    tbMaestroAlmacen: List[TbMaestroAlmacen] = field(default_factory=list, metadata={'sa': relationship('TbMaestroAlmacen', uselist=True, back_populates='tbMaestroPais')})
    tbMaestroCentroGestion: List[TbMaestroCentroGestion] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCentroGestion', uselist=True, back_populates='tbMaestroPais')})
    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroPais')})
    tbMaestroEmpresa: List[TbMaestroEmpresa] = field(default_factory=list, metadata={'sa': relationship('TbMaestroEmpresa', uselist=True, back_populates='tbMaestroPais')})
    tbMaestroOperario: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, foreign_keys='[TbMaestroOperario.IDPais]', back_populates='tbMaestroPais')})
    tbMaestroOperario_: List[TbMaestroOperario] = field(default_factory=list, metadata={'sa': relationship('TbMaestroOperario', uselist=True, foreign_keys='[TbMaestroOperario.IdPaisNacimiento]', back_populates='tbMaestroPais_')})
    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroPais')})
    tbMaestroMotivoNoAsegurado: Optional[TbMaestroMotivoNoAsegurado] = field(default=None, metadata={'sa': relationship('TbMaestroMotivoNoAsegurado', back_populates='tbMaestroPais')})
    tbMaestroPersonaContacto: List[TbMaestroPersonaContacto] = field(default_factory=list, metadata={'sa': relationship('TbMaestroPersonaContacto', uselist=True, back_populates='tbMaestroPais')})


@mapper_registry.mapped
@dataclass
class TbMaestroTarifa:
    __tablename__ = 'tbMaestroTarifa'
    __table_args__ = (
        ForeignKeyConstraint(['IDEstado'], ['tbMaestroTarifaEstado.IDEstado'], name='FK_tbMaestroTarifa_tbMaestroTarifaEstado'),
        ForeignKeyConstraint(['IDMoneda'], ['tbMaestroMoneda.IDMoneda'], name='FK_tbMaestroTarifa_tbMaestroMoneda'),
        PrimaryKeyConstraint('IDTarifa', name='PK_tbMaestroTarifa')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTarifa: str = field(metadata={'sa': mapped_column(Unicode(10))})
    IDMoneda: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    MaxPrioridad: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    TarifaPVP: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescTarifa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDEstado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaDesde: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaHasta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    IDTarifaOrigen: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IdContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDTipoTarifa: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer, server_default=text('((0))'))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCentroGestion: List[TbMaestroCentroGestion] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCentroGestion', uselist=True, back_populates='tbMaestroTarifa')})
    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroTarifa')})
    tbMaestroTarifaEstado: Optional[TbMaestroTarifaEstado] = field(default=None, metadata={'sa': relationship('TbMaestroTarifaEstado', back_populates='tbMaestroTarifa')})
    tbMaestroMoneda: Optional[TbMaestroMoneda] = field(default=None, metadata={'sa': relationship('TbMaestroMoneda', back_populates='tbMaestroTarifa')})


@mapper_registry.mapped
@dataclass
class TbMaestroTipoCliente:
    __tablename__ = 'tbMaestroTipoCliente'
    __table_args__ = (
        ForeignKeyConstraint(['IDMotivoNoAsegurado'], ['tbMaestroMotivoNoAsegurado.IDMotivo'], name='FK_IDMotivoNoAsegurado_tbMaestroTipoCliente_tbMaestroMotivoNoAsegurado'),
        PrimaryKeyConstraint('IDTipoCliente', name='PK_tbMaestroTipoCliente')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoCliente: str = field(metadata={'sa': mapped_column(Unicode(10))})
    Estadistica: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    ExcluirSilicie: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ExcluirDestinoSilicie: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    DescTipoCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDMotivoNoAsegurado: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCliente: List[TbMaestroCliente] = field(default_factory=list, metadata={'sa': relationship('TbMaestroCliente', uselist=True, back_populates='tbMaestroTipoCliente')})
    tbMaestroMotivoNoAsegurado: Optional[TbMaestroMotivoNoAsegurado] = field(default=None, metadata={'sa': relationship('TbMaestroMotivoNoAsegurado', back_populates='tbMaestroTipoCliente')})


@mapper_registry.mapped
@dataclass
class TbMaestroTipoFactura:
    __tablename__ = 'tbMaestroTipoFactura'
    __table_args__ = (
        ForeignKeyConstraint(['IDAgrupacion'], ['tbMaestroAgrupacion.IDAgrupacion'], name='FK_tbMaestroTipoFactura_tbMaestroAgrupacion'),
        PrimaryKeyConstraint('IDTipoFactura', name='PK_tbMaestroTipoFactura')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoFactura: int = field(metadata={'sa': mapped_column(Integer)})
    DescTipoFactura: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDAgrupacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroAgrupacion: Optional[TbMaestroAgrupacion] = field(default=None, metadata={'sa': relationship('TbMaestroAgrupacion', back_populates='tbMaestroTipoFactura')})
    tbMaestroTipoClasif: List[TbMaestroTipoClasif] = field(default_factory=list, metadata={'sa': relationship('TbMaestroTipoClasif', uselist=True, back_populates='tbMaestroTipoFactura')})


@mapper_registry.mapped
@dataclass
class TbObraEstadoPresupuesto:
    __tablename__ = 'tbObraEstadoPresupuesto'
    __table_args__ = (
        ForeignKeyConstraint(['IDEstadoVenta'], ['tbCRMEstadoVenta.IDEstadoVenta'], name='FK_tbObraEstadoPresupuesto_tbCRMEstadoVenta'),
        PrimaryKeyConstraint('IDEstado', name='PK_tbObraEstadoPresupuesto')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDEstado: int = field(metadata={'sa': mapped_column(Integer)})
    DescEstado: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    Sistema: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    IDEstadoVenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbObraPresupCabecera: List[TbObraPresupCabecera] = field(default_factory=list, metadata={'sa': relationship('TbObraPresupCabecera', uselist=True, back_populates='tbObraEstadoPresupuesto')})
    tbCRMEstadoVenta: Optional[TbCRMEstadoVenta] = field(default=None, metadata={'sa': relationship('TbCRMEstadoVenta', back_populates='tbObraEstadoPresupuesto')})


@mapper_registry.mapped
@dataclass
class TbOfertaComercialEstado:
    __tablename__ = 'tbOfertaComercialEstado'
    __table_args__ = (
        ForeignKeyConstraint(['IDEstadoVenta'], ['tbCRMEstadoVenta.IDEstadoVenta'], name='FK_tbOfertaComercialEstado_tbCRMEstadoVenta'),
        PrimaryKeyConstraint('IDEstado', name='PK_tbOfertaComercialEstado')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDEstado: int = field(metadata={'sa': mapped_column(Integer)})
    DescEstado: str = field(metadata={'sa': mapped_column(Unicode(100), nullable=False)})
    LanzarAccion: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Sistema: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ModificarOferta: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDEstadoVenta: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(2))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbCRMEstadoVenta: Optional[TbCRMEstadoVenta] = field(default=None, metadata={'sa': relationship('TbCRMEstadoVenta', back_populates='tbOfertaComercialEstado')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbOfertaComercialEstado')})


@mapper_registry.mapped
@dataclass
class TbMaestroPersonaContacto:
    __tablename__ = 'tbMaestroPersonaContacto'
    __table_args__ = (
        ForeignKeyConstraint(['IDCargo'], ['tbMaestroCargo.IDCargo'], name='FK_tbMaestroPersonaContacto_tbMaestroCargo'),
        ForeignKeyConstraint(['IDClienteActual'], ['tbMaestroCliente.IDCliente'], name='FK_tbMaestroPersonaContacto_tbMaestroCliente'),
        ForeignKeyConstraint(['IDPais'], ['tbMaestroPais.IDPais'], name='FK_tbMaestroPersonaContacto_tbMaestroPais'),
        PrimaryKeyConstraint('IDPersonaContacto', name='PK_tbMaestroPersonaContacto')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDPersonaContacto: int = field(metadata={'sa': mapped_column(Integer)})
    AltaAutomatica: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Nombre: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    Apellidos: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    FechaNacimiento: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    Sexo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    Direccion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    CodPostal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Poblacion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Provincia: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    IDPais: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    TelefonoPersonal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    FaxPersonal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    EmailPersonal: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Comentarios: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(300))})
    IDCargo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(3))})
    IDClienteActual: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    FechaAltaCliente: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCargo: Optional[TbMaestroCargo] = field(default=None, metadata={'sa': relationship('TbMaestroCargo', back_populates='tbMaestroPersonaContacto')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbMaestroPersonaContacto')})
    tbMaestroPais: Optional[TbMaestroPais] = field(default=None, metadata={'sa': relationship('TbMaestroPais', back_populates='tbMaestroPersonaContacto')})
    tbClientePersonaContacto: List[TbClientePersonaContacto] = field(default_factory=list, metadata={'sa': relationship('TbClientePersonaContacto', uselist=True, back_populates='tbMaestroPersonaContacto')})


@mapper_registry.mapped
@dataclass
class TbMaestroTipoClasif:
    __tablename__ = 'tbMaestroTipoClasif'
    __table_args__ = (
        ForeignKeyConstraint(['IDTipoFactura'], ['tbMaestroTipoFactura.IDTipoFactura'], name='FK_tbMaestroTipoClasif_tbMaestroTipoFactura'),
        PrimaryKeyConstraint('IDTipoClasif', name='PK_tbMaestroTipoClasif')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDTipoClasif: str = field(metadata={'sa': mapped_column(Unicode(10))})
    IDTipoFactura: int = field(metadata={'sa': mapped_column(Integer, nullable=False)})
    DescTipoClasif: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Prefijo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroProveedor: List[TbMaestroProveedor] = field(default_factory=list, metadata={'sa': relationship('TbMaestroProveedor', uselist=True, back_populates='tbMaestroTipoClasif')})
    tbMaestroTipoFactura: Optional[TbMaestroTipoFactura] = field(default=None, metadata={'sa': relationship('TbMaestroTipoFactura', back_populates='tbMaestroTipoClasif')})


@mapper_registry.mapped
@dataclass
class TbClientePersonaContacto:
    __tablename__ = 'tbClientePersonaContacto'
    __table_args__ = (
        ForeignKeyConstraint(['IDCargo'], ['tbMaestroCargo.IDCargo'], name='FK_tbClientePersonaContacto_tbMaestroCargo'),
        ForeignKeyConstraint(['IDCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbClientePersonaContacto_tbMaestroCliente'),
        ForeignKeyConstraint(['IDPersonaContacto'], ['tbMaestroPersonaContacto.IDPersonaContacto'], name='FK_tbClientePersonaContacto_tbMaestroPersonaContacto'),
        PrimaryKeyConstraint('IDPersona', name='PK_tbClientePersonaContacto'),
        Index('IX_tbClientePersonaContacto_IDCliente', 'IDCliente')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDPersona: int = field(metadata={'sa': mapped_column(Integer)})
    IDCliente: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    Predeterminada: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    Activo: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((1))'))})
    Nombre: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    Telefono1: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Telefono2: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Fax: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    Email: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(100))})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDCargo: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(3))})
    IDPersonaContacto: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})

    tbMaestroCargo: Optional[TbMaestroCargo] = field(default=None, metadata={'sa': relationship('TbMaestroCargo', back_populates='tbClientePersonaContacto')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbClientePersonaContacto')})
    tbMaestroPersonaContacto: Optional[TbMaestroPersonaContacto] = field(default=None, metadata={'sa': relationship('TbMaestroPersonaContacto', back_populates='tbClientePersonaContacto')})
    tbOfertaComercialCabecera: List[TbOfertaComercialCabecera] = field(default_factory=list, metadata={'sa': relationship('TbOfertaComercialCabecera', uselist=True, back_populates='tbClientePersonaContacto')})


@mapper_registry.mapped
@dataclass
class TbOfertaComercialCabecera:
    __tablename__ = 'tbOfertaComercialCabecera'
    __table_args__ = (
        ForeignKeyConstraint(['IDCentroGestion'], ['tbMaestroCentroGestion.IDCentroGestion'], name='FK_tbOfertaComercialCabecera_tbMaestroCentroGestion'),
        ForeignKeyConstraint(['IDCliente'], ['tbMaestroCliente.IDCliente'], name='FK_tbOfertaComercialCabecera_tbMaestroCliente'),
        ForeignKeyConstraint(['IDCondicionEnvio'], ['tbMaestroCondicionEnvio.IDCondicionEnvio'], name='FK_tbOfertaComercialCabecera_tbMaestroCondicionEnvio'),
        ForeignKeyConstraint(['IDCondicionPago'], ['tbMaestroCondicionPago.IDCondicionPago'], name='FK_tbOfertaComercialCabecera_tbMaestroCondicionPago'),
        ForeignKeyConstraint(['IDDireccionCliente'], ['tbClienteDireccion.IDDireccion'], name='FK_tbOfertaComercialCabecera_tbClienteDireccion'),
        ForeignKeyConstraint(['IDEmpresa'], ['tbMaestroEmpresa.IDEmpresa'], name='FK_tbOfertaComercialCabecera_tbMaestroEmpresa'),
        ForeignKeyConstraint(['IDEstadoOferta'], ['tbOfertaComercialEstado.IDEstado'], name='FK_tbOfertaComercialCabecera_tbOfertaComercialEstado'),
        ForeignKeyConstraint(['IDFormaEnvio'], ['tbMaestroFormaEnvio.IDFormaEnvio'], name='FK_tbOfertaComercialCabecera_tbMaestroFormaEnvio'),
        ForeignKeyConstraint(['IDFormaPago'], ['tbMaestroFormaPago.IDFormaPago'], name='FK_tbOfertaComercialCabecera_tbMaestroFormaPago'),
        ForeignKeyConstraint(['IDModoTransporte'], ['tbMaestroModoTrasporte.IDModoTransporte'], name='FK_tbOfertaComercialCabecera_tbMaestroModoTrasporte'),
        ForeignKeyConstraint(['IDMoneda'], ['tbMaestroMoneda.IDMoneda'], name='FK_tbOfertaComercialCabecera_tbMaestroMoneda'),
        ForeignKeyConstraint(['IDObra'], ['tbObraCabecera.IDObra'], name='FK_tbOfertaComercialCabecera_tbObraCabecera'),
        ForeignKeyConstraint(['IDOperario'], ['tbMaestroOperario.IDOperario'], name='FK_tbOfertaComercialCabecera_tbMaestroOperario'),
        ForeignKeyConstraint(['IDPersona'], ['tbClientePersonaContacto.IDPersona'], name='FK_PersonaContacto'),
        ForeignKeyConstraint(['IDTipoOferta'], ['tbOfertaComercialTipo.IDTipoOfertaComercial'], name='FK_tbOfertaComercialCabecera_tbOfertaComercialTipo'),
        PrimaryKeyConstraint('IDOfertaComercial', name='PK_tbOfertaComercialCabecera')
    )
    __sa_dataclass_metadata_key__ = 'sa'

    IDOfertaComercial: int = field(metadata={'sa': mapped_column(Integer)})
    NumOferta: str = field(metadata={'sa': mapped_column(Unicode(25), nullable=False)})
    RevOferta: int = field(metadata={'sa': mapped_column(Integer, nullable=False)})
    FechaOferta: datetime = field(metadata={'sa': mapped_column(DateTime, nullable=False)})
    DescOfertaComercial: str = field(metadata={'sa': mapped_column(Unicode(300), nullable=False)})
    IDTipoOferta: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    IDEstadoOferta: int = field(metadata={'sa': mapped_column(Integer, nullable=False)})
    FechaEstado: datetime = field(metadata={'sa': mapped_column(DateTime, nullable=False)})
    IDMoneda: str = field(metadata={'sa': mapped_column(Unicode(10), nullable=False)})
    CambioA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    CambioB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    VigenciaQConsumida: bool = field(metadata={'sa': mapped_column(Boolean, nullable=False, server_default=text('((0))'))})
    ImpCosteOferta: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpCosteOfertaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpCosteOfertaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    MargenOfertaTrabajo: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpOfertaVenta: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpOfertaVentaA: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    ImpOfertaVentaB: Decimal = field(metadata={'sa': mapped_column(Numeric(23, 8), nullable=False, server_default=text('((0))'))})
    IDContador: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCentroGestion: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDEmpresa: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDDireccionEmpresa: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(25))})
    IDDireccionCliente: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    FechaValidez: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    PlazoEntrega: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50), server_default=text("(N'A concretar tras la recepción de su pedido')"))})
    IDFormaPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCondicionPago: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDFormaEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDCondicionEnvio: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    IDModoTransporte: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    FechaInicioOferta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaFinOferta: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaCreacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    FechaModificacionAudi: Optional[datetime] = field(default=None, metadata={'sa': mapped_column(DateTime)})
    UsuarioAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    Texto: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})
    IDObra: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    IDOperario: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(10))})
    GradoAvanceManual: Optional[Decimal] = field(default=None, metadata={'sa': mapped_column(Numeric(23, 8))})
    RutaFicheroPresupuestos: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(250))})
    NOfertaComercialCliente: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(50))})
    UsuarioCreacionAudi: Optional[str] = field(default=None, metadata={'sa': mapped_column(Unicode(75))})
    IDPersona: Optional[int] = field(default=None, metadata={'sa': mapped_column(Integer)})
    Observaciones: Optional[str] = field(default=None, metadata={'sa': mapped_column(NTEXT(1073741823))})

    tbMaestroCentroGestion: Optional[TbMaestroCentroGestion] = field(default=None, metadata={'sa': relationship('TbMaestroCentroGestion', back_populates='tbOfertaComercialCabecera')})
    tbMaestroCliente: Optional[TbMaestroCliente] = field(default=None, metadata={'sa': relationship('TbMaestroCliente', back_populates='tbOfertaComercialCabecera')})
    tbMaestroCondicionEnvio: Optional[TbMaestroCondicionEnvio] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionEnvio', back_populates='tbOfertaComercialCabecera')})
    tbMaestroCondicionPago: Optional[TbMaestroCondicionPago] = field(default=None, metadata={'sa': relationship('TbMaestroCondicionPago', back_populates='tbOfertaComercialCabecera')})
    tbClienteDireccion: Optional[TbClienteDireccion] = field(default=None, metadata={'sa': relationship('TbClienteDireccion', back_populates='tbOfertaComercialCabecera')})
    tbMaestroEmpresa: Optional[TbMaestroEmpresa] = field(default=None, metadata={'sa': relationship('TbMaestroEmpresa', back_populates='tbOfertaComercialCabecera')})
    tbOfertaComercialEstado: Optional[TbOfertaComercialEstado] = field(default=None, metadata={'sa': relationship('TbOfertaComercialEstado', back_populates='tbOfertaComercialCabecera')})
    tbMaestroFormaEnvio: Optional[TbMaestroFormaEnvio] = field(default=None, metadata={'sa': relationship('TbMaestroFormaEnvio', back_populates='tbOfertaComercialCabecera')})
    tbMaestroFormaPago: Optional[TbMaestroFormaPago] = field(default=None, metadata={'sa': relationship('TbMaestroFormaPago', back_populates='tbOfertaComercialCabecera')})
    tbMaestroModoTrasporte: Optional[TbMaestroModoTrasporte] = field(default=None, metadata={'sa': relationship('TbMaestroModoTrasporte', back_populates='tbOfertaComercialCabecera')})
    tbMaestroMoneda: Optional[TbMaestroMoneda] = field(default=None, metadata={'sa': relationship('TbMaestroMoneda', back_populates='tbOfertaComercialCabecera')})
    tbObraCabecera: Optional[TbObraCabecera] = field(default=None, metadata={'sa': relationship('TbObraCabecera', back_populates='tbOfertaComercialCabecera')})
    tbMaestroOperario: Optional[TbMaestroOperario] = field(default=None, metadata={'sa': relationship('TbMaestroOperario', back_populates='tbOfertaComercialCabecera')})
    tbClientePersonaContacto: Optional[TbClientePersonaContacto] = field(default=None, metadata={'sa': relationship('TbClientePersonaContacto', back_populates='tbOfertaComercialCabecera')})
    tbOfertaComercialTipo: Optional[TbOfertaComercialTipo] = field(default=None, metadata={'sa': relationship('TbOfertaComercialTipo', back_populates='tbOfertaComercialCabecera')})
