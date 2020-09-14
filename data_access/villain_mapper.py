from config import conn
from domain.villain_domain import Vilao

class VilaoMapper():
    def listar_viloes(self):
        cur = conn.cursor()
        sql = f'SELECT * FROM vilao'
        cur.execute(sql)
        rows = cur.fetchall()
        viloes = []
        for i in range(len(rows)):
            vilao = Vilao(*rows[i])
            viloes.append(vilao)
        return viloes

    def buscar_vilao(self, nome):
        cur = conn.cursor()
        sql = f'SELECT * FROM vilao WHERE nome="{nome}"'
        cur.execute(sql)
        rows = cur.fetchall()
        return Vilao(*rows[0])
    
    def buscar_vilao_por_id(self, vilao_id):
        cur = conn.cursor()
        sql = f'SELECT * FROM vilao WHERE id={vilao_id}'
        cur.execute(sql)
        rows = cur.fetchall()
        return Vilao(*rows[0])
    
    def inserir_vilao(self, vilao):
        cur = conn.cursor()
        sql = f'insert into vilao (nome, vida) values ("{vilao.nome}", {vilao.vida});'
        cur.execute(sql)
        conn.commit()

    def atualizar_vilao(self, nome, vida):
        cur = conn.cursor()
        sql = f'update vilao set vida={vida} where nome="{nome}");'
        cur.execute(sql)
        conn.commit()
''' 
con = sqlite3.connect('base.db')

cur = con.cursor()

sql = """
CREATE TABLE carros (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)"""

cur.execute(sql)
con.commit()
con.close()
'''