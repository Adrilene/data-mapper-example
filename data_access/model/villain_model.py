from sqlalchemy import Table, Column, Integer, String
from config.settings import meta


vilao = Table("vilao",
     meta,
     Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
     Column("nome", String(50), nullable=False, unique=True),
     Column("vida", Integer, nullable=False),
)

'''CREATE TABLE vilao (
	id INTEGER NOT NULL, 
	nome VARCHAR(50) NOT NULL, 
	vida INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (nome)
)'''