from sqlalchemy import Table, Column, Integer, String, ForeignKey
from config import meta

'''class Heroi(engine.Model):  
    __tablename__ = "heroi"

    id = engine.Column(engine.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = engine.Column(engine.String(50), nullable=False)
    cidade_id = engine.Column(engine.Integer, engine.ForeignKey("cidade.id"), nullable=False)
    forca = engine.Column(engine.Integer, nullable=False)'''

heroi = Table("heroi",
     meta,
     Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
     Column("nome", String(50), nullable=False),
     Column("cidade_id", Integer, ForeignKey("cidade.id")),
     Column("poder", String(50), nullable=False),
     Column("forca", Integer, nullable=False),
)