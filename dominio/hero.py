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

class Heroi():
    def __init__(self, nome, cidade, poder, viloes, vida, forca):
        self.__nome = nome
        self.cidade = cidade
        self.poder = poder
        self.forca = forca

    def salvar_cidade(self):
        '''
            select de cidades atacadas and cidade == self.cidade
            pega só o campo vilão
        '''
        return vilao
    
    def atacar_vilao(self, vilao):
        '''
            select de cidades atacadas and cidade == self.cidade
        '''
        pass
