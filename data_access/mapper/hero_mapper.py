from config.settings import conn
from domain.hero_domain import Heroi
from .city_mapper import CidadeMapper


class HeroiMapper():
    def listar_herois(self):
        cur = conn.cursor()
        sql = f'SELECT * FROM heroi'
        cur.execute(sql)
        rows = cur.fetchall()
        herois = []
        for row in rows:
            cidade = CidadeMapper().buscar_cidade_por_id(row[2])
            heroi = Heroi(row[1], cidade.nome, row[2], row[3])
            herois.append(heroi)
        cur.close()
        return herois

    def buscar_heroi(self, nome):
        cur = conn.cursor()
        sql = f'SELECT * FROM heroi WHERE nome="{nome}"'
        cur.execute(sql)
        row = cur.fetchone()
        cidade = CidadeMapper().buscar_cidade_por_id(row[2])
        heroi = Heroi(row[1], cidade.nome, row[3], row[4])
        cur.close()
        return heroi

    def inserir_heroi(self, heroi):
        try:
            cidade = CidadeMapper().buscar_cidade(heroi.cidade)
            cur = conn.cursor()
            sql = f'insert into heroi (nome, cidade_id, poder, forca) values ("{heroi.nome}", "{cidade.id}", "{heroi.poder}", "{heroi.forca}");'
            cur.execute(sql)
            conn.commit()
            cur.close()
        except:
            pass

