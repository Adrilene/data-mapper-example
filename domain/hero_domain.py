'''
Classe herói 
    nome
    cidade
    super poder
    vilões
    vida
    forca
atacar-vilao
escolher-vilao --> pega lista vilões vivos -> aleatório
'''
import random
from data_access import city_mapper, hero_mapper, villain_mapper


class Heroi():
    def __init__(self, nome, cidade, poder, forca):
        self.__nome = nome
        self.cidade = cidade
        self.poder = poder
        self.forca = forca

    def salvar_cidade(self):
        cidade_map = city_mapper.Cidade()
        vilao_map = villain_mapper.Vilao()
        cidade = cidade_map.buscar_cidade(self.cidade)
        if cidade.ataque:
            vilao = vilao_map.buscar_vilao(cidade.vilao)
            return vilao

    def atacar_vilao(self, vilao):
        vilao = vilao_map.buscar_vilao(vilao.nome)
        nova_vida = vilao.vida - self.forca
        vilao_map.atualizar_vilao(vilao.nome, nova_vida)
