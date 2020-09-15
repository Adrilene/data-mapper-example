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
        cidade = cidade_map.buscar_cidade(self.cidade)
        if cidade.ataque:
            vilao_map = villain_mapper.VilaoMapper()
            vilao = vilao_map.buscar_vilao(cidade.vilao)
            return vilao

    def atacar_vilao(self, vilao):
        vilao_map = villain_mapper.VilaoMapper()
        vilao.vida -= self.forca
        vilao_map.atualizar_vilao(vilao.nome, vilao.vida)
        return vilao


'''
objeto salva o nome
banco salva o id
'''