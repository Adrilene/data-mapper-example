from sqlalchemy import Table, Column, Boolean, Integer, String, ForeignKey
from config.settings import meta


cidade = Table("cidade",
     meta,
     Column("id", Integer, primary_key=True, nullable=False, autoincrement=True),
     Column("nome", String(50), nullable=False, unique=True),
     Column("ataque", Boolean),
     Column("vilao_id", Integer, ForeignKey("vilao.id")),
     sqlite_autoincrement=True
)


'''
CREATE TABLE cidade (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	nome VARCHAR(50) NOT NULL, 
	ataque BOOLEAN, 
	vilao_id INTEGER, 
	UNIQUE (nome), 
	CHECK (ataque IN (0, 1)), 
	FOREIGN KEY(vilao_id) REFERENCES vilao (id)
))
'''