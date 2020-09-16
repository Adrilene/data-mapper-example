from sqlalchemy import create_engine, MetaData
import sqlite3


engine = create_engine("sqlite:///app.db")
meta = MetaData()
meta.bind = engine

conn = sqlite3.connect('app.db')

