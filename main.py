import os
#os.remove('app.db')
from config import meta, engine
from data_access.model import city_model, hero_model, villain_model
meta.create_all(engine)
from menu_hero import heroi_menu
from menu_villain import vilao_menu



if __name__ == "__main__":
    meta.create_all(engine)

    print('========= HERO X VILLAIN =========')
    print('Faça sua escolha!!!')
    print('(0) Herói')
    print('(1) Vilão')
    escolha = int(input())
    if escolha == 0:
        heroi_menu()
    else:
        vilao_menu()
