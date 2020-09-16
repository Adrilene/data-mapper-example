from config.settings import conn
from domain.villain_domain import Vilao

class VilaoMapper():
    def listar_viloes(self):
        cur = conn.cursor()
        sql = f'SELECT * FROM vilao'
        cur.execute(sql)
        rows = cur.fetchall()
        viloes = []
        for row in rows:
            vilao = Vilao(*row[1:])
            viloes.append(vilao)
        cur.close()
        return viloes

    def buscar_vilao(self, nome):
        cur = conn.cursor()
        sql = f'SELECT * FROM vilao WHERE nome="{nome}"'
        cur.execute(sql)
        row = cur.fetchone()
        vilao = Vilao(*row[1:])
        vilao.id = row[0]
        return vilao

    def buscar_vilao_por_id(self, vilao_id):
        cur = conn.cursor()
        sql = f'SELECT * FROM vilao WHERE id={vilao_id}'
        cur.execute(sql)
        row = cur.fetchone()
        vilao = Vilao(row[1], row[2])
        vilao.id = row[0]
        return vilao
    
    def inserir_vilao(self, vilao):
        try:
            cur = conn.cursor()
            sql = f'insert into vilao (nome, vida) values ("{vilao.nome}", {vilao.vida});'
            cur.execute(sql)
            conn.commit()
        except:
            pass

    def atualizar_vilao(self, nome, vida):
        cur = conn.cursor()
        sql = f'update vilao set vida={vida} where nome="{nome}";'
        cur.execute(sql)
        conn.commit()

    def delete_vilao(self, nome):
        cur = conn.cursor()
        sql = f'delete from vilao where nome="{nome}";'
        cur.execute(sql)
        conn.commit()

    def get_id(self, vilao):
        cur = conn.cursor()
        sql = f'select id from vilao where nome="{vilao.nome}";'
        cur.execute(sql)
        return cur.fetchone()[0]
