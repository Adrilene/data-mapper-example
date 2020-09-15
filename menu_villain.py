from mapping import cidade_map, heroi_map, vilao_map


def vilao_menu():
    print('=== DESTRUA A CIDADE ===')
    print('Escolha seu vilão')
    viloes = vilao_map.listar_viloes()
    nomes_viloes = [vilao.nome for vilao in viloes]
    print(f'Vilões: {nomes_viloes}')
    nome = input()
    vilao = vilao_map.buscar_vilao(nome)
    print('Escolha uma cidade para atacar:')
    cidades = cidade_map.listar_cidades()
    nomes_cidades = [cidade.nome for cidade in cidades]
    print(f'Cidades: {nomes_cidades}')
    cidade_atacada = input()
    cidade_atacada = [cidade for cidade in cidades if cidade_atacada == cidade.nome][0]

    vilao.atacar_cidade(cidade_atacada)
    cidade = cidade_map.buscar_cidade(cidade_atacada.nome)
    vilao = vilao_map.buscar_vilao_por_id(vilao.id)
    
    print('Status da cidade:')
    print(f'Nome:{cidade.nome}, Sob_ataque:{cidade.ataque}, Id_Vilão:{cidade.vilao}, Vilão:{vilao.nome}')
    print('FIM')
