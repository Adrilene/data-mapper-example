import random
from data_access import city_mapper, hero_mapper, villain_mapper


class Heroi():
    def __init__(self, nome, cidade, poder, forca):
        self.nome = nome
        self.cidade = cidade
        self.poder = poder
        self.forca = forca

    def salvar_cidade(self):
        cidade_map = city_mapper.CidadeMapper()
        vilao_map = villain_mapper.VilaoMapper()
        cidade = cidade_map.buscar_cidade_por_id(self.cidade)
        if cidade.ataque:
            vilao = vilao_map.buscar_vilao(cidade.vilao)
            return vilao

    def atacar_vilao(self, vilao):
        vilao = vilao_map.buscar_vilao(vilao.nome)
        nova_vida = vilao.vida - self.forca
        vilao_map.atualizar_vilao(vilao.nome, nova_vida)
