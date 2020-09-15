from sqlalchemy import Table, Column, Integer, String
from config import meta

'''class Vilao(engine.Model):
    __tablename__ = "vilao"

    id = engine.Column(engine.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = engine.Column(engine.String(50), nullable=False)
    vida = engine.Column(engine.Integer, nullable=False)'''

vilao = Table("vilao",
     meta,
     Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
     Column("nome", String(50), nullable=False, unique=True),
     Column("vida", Integer, nullable=False),
)