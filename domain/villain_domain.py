'''
Classe vilao
    nome
    cidade
    super poder
    herois
    vida
atacar-heroi
escolher-vilao --> pega lista vilões vivos -> aleatório
'''

class Vilao():
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar_cidade(self, cidade):
        cidade.sob_ataque(self)
