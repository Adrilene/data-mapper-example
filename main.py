import sqlite3
from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:///app.db")
meta = MetaData()

#con = sqlite3.connect('base.db')
#con.close()