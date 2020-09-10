from ...main import meta
from sqlalchemy import Talbe, Column, Boolean, Integer, String
from villain import Vilao

Tale("cidade",
     meta,
     Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
     Column("nome", String(50), nullable=False),
     Column("ataque", Boolean, nullable=False),
     Column("vilao_id", Integer, ForeignKey("vilao.id")),
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