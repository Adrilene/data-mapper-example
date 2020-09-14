from domain.city_domain import Cidade
from domain.hero_domain import Heroi
from domain.villain_domain import Vilao


gothan = Cidade(nome='gothan', ataque=False, vilao=None)
central_city = Cidade(nome='central_city', ataque=False, vilao=None)

batman = Heroi(nome='batman',
                cidade='gothan',
                poder='super_rico',
                forca=50)

flash = Heroi(nome='flash',
                cidade='central_city',
                poder='rápido',
                forca=80)

coringa = Vilao(nome='coringa',
                vida=500)