from config import conn
from domain.hero_domain import Heroi
from .city_mapper import CidadeMapper


class HeroiMapper():
    def listar_herois(self):
        cur = conn.cursor()
        sql = f'SELECT * FROM heroi'
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        herois = []
        for i in range(len(rows)):
            cidade = CidadeMapper().buscar_cidade_por_id(rows[0][3])
            heroi = Heroi(rows[0][1], cidade.nome, rows[0][3], rows[0][4])
            herois.append(heroi)
        return herois

    def buscar_heroi(self, nome):
        cur = conn.cursor()
        sql = f'SELECT * FROM heroi WHERE nome="{nome}"'
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        cidade = CidadeMapper().buscar_cidade_por_id(rows[0][3])
        heroi = Heroi(rows[0][1], cidade.nome, rows[0][3], rows[0][4])
        return heroi

    def inserir_heroi(self, heroi):
        import ipdb; ipdb.set_trace()
        cidade = CidadeMapper().buscar_cidade(heroi.cidade)
        cur = conn.cursor()
        sql = f'insert into heroi (nome, forca, cidade_id) values ("{heroi.nome}", "{heroi.forca}", "{cidade_id}");'
        cur.execute(sql)
        conn.commit()
        cur.close()
