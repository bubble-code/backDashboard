from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OfertaComercial(db.Model):
    __tablename__ = 'tbOfertaCabecera'
    