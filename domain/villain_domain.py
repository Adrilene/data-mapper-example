from data_access.mapper import villain_mapper


class Vilao():
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar_cidade(self, cidade):
        vilao_map = villain_mapper.VilaoMapper()
        id = vilao_map.get_id(self)
        cidade.sob_ataque(id)
