from config import conn
from domain.city_domain import Cidade
from .villain_mapper import VilaoMapper


class CidadeMapper():
    def listar_cidades(self):
        cur = conn.cursor()
        sql = f'SELECT * FROM cidade'
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        cidades = []
        for i in range(len(rows)):
            vilao = VilaoMapper().buscar_vilao_por_id(rows[0][3])
            cidade = Cidade(rows[0][1], rows[0][2], vilao.nome)
            cidades.append(cidade)
        
        return cidades

    def buscar_cidade(self, nome):
        cur = conn.cursor()
        sql = f'SELECT * FROM cidade WHERE nome="{nome}"'
        cur.execute(sql)
        rows = cur.fetchall()
        vilao = VilaoMapper().buscar_vilao_por_id(rows[0][3])
        cur.close()
        cidade = Cidade(rows[0][1], rows[0][2], vilao.nome)
        return cidade
    
    def buscar_cidade_por_id(self, cidade_id):
        cur = conn.cursor()
        sql = f'SELECT * FROM cidade WHERE nome="{nome}"'
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        return Cidade(*rows)

    def inserir_cidade(self, cidade):
        cur = conn.cursor()
        sql = ''
        if cidade.ataque:
            vilao_id = VilaoMapper().buscar_vilao(cidade.vilao)
            sql = f'insert into cidade (nome, ataque, vilao_id) values ("{cidade.nome}", {cidade.ataque}, {vilao_id});'
        else:
            sql = f'insert into cidade (nome, ataque) values ("{cidade.nome}", {cidade.ataque});'
        cur.execute(sql)
        conn.commit()
        cur.close()
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