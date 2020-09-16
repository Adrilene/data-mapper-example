from config.settings import conn
from domain.city_domain import Cidade
from .villain_mapper import VilaoMapper


class CidadeMapper():
    def listar_cidades(self):
        cur = conn.cursor()
        sql = f'SELECT * FROM cidade;'
        cur.execute(sql)
        rows = cur.fetchall()
        cidades = []
        for row in rows:
            cidade = Cidade(*row[1:])
            cidade.id = row[0]
            cidades.append(cidade)
        cur.close()
        return cidades

    def buscar_cidade(self, nome):
        cur = conn.cursor()
        sql = f'SELECT * FROM cidade WHERE nome="{nome}"'
        cur.execute(sql)
        row = cur.fetchone()
        if row[2]:
            vilao = VilaoMapper().buscar_vilao_por_id(row[2])
            cidade = Cidade(row[1], row[2], vilao.nome)
        else:
            cidade = Cidade(row[1], row[2], None)
        cidade.id = row[0]
        cur.close()
        return cidade

    def buscar_cidade_por_id(self, cidade_id):
        cur = conn.cursor()
        sql = f'SELECT * FROM cidade WHERE id="{cidade_id}"'
        cur.execute(sql)
        row = cur.fetchone()
        cidade = Cidade(*row[1:])
        cidade.id = row[0]
        cur.close()
        return cidade

    def inserir_cidade(self, cidade):
        try:
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
        except:
            pass

    def atualizar_cidade(self, cidade, vilao_id):
        cur = conn.cursor()
        if not vilao_id:           
            sql = f'update cidade set ataque={cidade.ataque}, vilao_id=NULL where nome="{cidade.nome}";'
        else: 
            sql = f'update cidade set ataque={cidade.ataque}, vilao_id={vilao_id} where nome="{cidade.nome}";'
        cur.execute(sql)
        conn.commit()
        cur.close()
