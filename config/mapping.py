from data_access.mapper.city_mapper import CidadeMapper
from data_access.mapper.hero_mapper import HeroiMapper
from data_access.mapper.villain_mapper import VilaoMapper
from config.domains import gothan, central_city, batman, flash, coringa


def mapping_init():
    vilao_map = VilaoMapper()
    vilao_map.inserir_vilao(coringa)

    cidade_map = CidadeMapper()
    cidade_map.inserir_cidade(gothan)
    cidade_map.inserir_cidade(central_city)

    heroi_map = HeroiMapper()
    heroi_map.inserir_heroi(batman)
    heroi_map.inserir_heroi(flash)

    return cidade_map, heroi_map, vilao_map