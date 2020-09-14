from data_access.city_mapper import CidadeMapper
from data_access.hero_mapper import HeroiMapper
from data_access.villain_mapper import VilaoMapper
from domains import gothan, central_city, batman, flash, coringa

vilao_map = VilaoMapper()
vilao_map.inserir_vilao(coringa)

cidade_map = CidadeMapper()
cidade_map.inserir_cidade(gothan)
cidade_map.inserir_cidade(central_city)

heroi_map = HeroiMapper()
heroi_map.inserir_heroi(batman)
heroi_map.inserir_heroi(flash)
import ipdb; ipdb.set_trace()

