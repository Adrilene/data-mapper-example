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
        from data_access.villain_mapper import VilaoMapper
        vilao_map = VilaoMapper()
        id = vilao_map.get_id(self)
        cidade.sob_ataque(id)
