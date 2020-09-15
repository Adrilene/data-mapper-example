class Cidade:
    def __init__(self, nome, ataque, vilao):
        self.nome = nome
        self.ataque = ataque
        self.vilao = vilao

    def sob_ataque(self, vilao):
        from data_access import city_mapper
        self.ataque = True
        self.vilao = vilao.id
        cidade = city_mapper.CidadeMapper()
        cidade.atualizar_cidade(self)
