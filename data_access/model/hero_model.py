from sqlalchemy import Table, Column, Integer, String, ForeignKey
from config.settings import meta


heroi = Table("heroi",
     meta,
     Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
     Column("nome", String(50), nullable=False, unique=True),
     Column("cidade_id", Integer, ForeignKey("cidade.id")),
     Column("poder", String(50), nullable=False),
     Column("forca", Integer, nullable=False),
)

'''
CREATE TABLE heroi (
	id INTEGER NOT NULL, 
	nome VARCHAR(50) NOT NULL, 
	cidade_id INTEGER, 
	poder VARCHAR(50) NOT NULL, 
	forca INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (nome), 
	FOREIGN KEY(cidade_id) REFERENCES cidade (id)
)
'''