from sqlalchemy import Table, Column, Boolean, Integer, String, ForeignKey
from config import meta


city = Table("cidade",
     meta,
     Column("id", Integer, primary_key=True, nullable=False, autoincrement=True),
     Column("nome", String(50), nullable=False),
     Column("ataque", Boolean),
     Column("vilao_id", Integer, ForeignKey("vilao.id")),
     sqlite_autoincrement=True
)


'''
baby_monitor_table = Table(
    "baby_monitor",
    self.meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("breathing", Boolean),
    Column("time_no_breathing", Integer),
    Column("crying", Boolean),
    Column("sleeping", Boolean),
)
self.meta.create_all(self.engine)
'''
'''
CREATE TABLE cidade (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
	nome VARCHAR(50) NOT NULL, 
	ataque BOOLEAN, 
	vilao_id INTEGER, 
	CHECK (ataque IN (0, 1)), 
	FOREIGN KEY(vilao_id) REFERENCES vilao (id)
)

CREATE TABLE heroi (
	id INTEGER NOT NULL, 
	nome VARCHAR(50) NOT NULL, 
	forca INTEGER NOT NULL, 
	cidade_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(cidade_id) REFERENCES cidade (id)
)

CREATE TABLE vilao (
	id INTEGER NOT NULL, 
	nome VARCHAR(50) NOT NULL, 
	vida INTEGER NOT NULL, 
	PRIMARY KEY (id)
)'''