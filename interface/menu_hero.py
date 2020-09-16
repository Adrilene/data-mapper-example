from config.mapping import mapping_init


def heroi_menu():
    cidade_map, heroi_map, vilao_map = mapping_init()
    print('=== SALVE A CIDADE ===')
    print('Escolha seu herói')
    herois = heroi_map.listar_herois()
    herois_nomes = [heroi.nome for heroi in herois]
    print(f'Heróis: {herois_nomes}')
    nome = input()
    heroi = heroi_map.buscar_heroi(nome)
    op = input('Verificar se sua cidade está sendo atacada? (s/n)')

    if op == 's':
        vilao = heroi.salvar_cidade()
        if vilao:
            print(f'Sim, {vilao.nome} está atacando.')
            escolha = input(f'Você deseja lutar ou fugir? (l/f)')

            while vilao.vida > 0 and escolha == 'l':
                print('Status do vilão')
                print(f'Vilão: {vilao.nome}')
                print(f'Vida: {vilao.vida}')
                vilao = heroi.atacar_vilao(vilao)
                escolha = input(f'Você deseja lutar ou fugir? (l/f)')

            if escolha == 'f':
                print('Você é um mau herói >:(')
                print('FIM')
            else:
                print(f'{vilao.nome} foi derrotado!!!')
                vilao_id = vilao_map.get_id(vilao)
                cidade = cidade_map.buscar_cidade(heroi.cidade)
                cidade.ataque = False
                cidade.vilao = None
                cidade_map.atualizar_cidade(cidade, vilao_id)
                vilao = vilao_map.delete_vilao(vilao.nome)
                print('Sua cidade está segura, parabéns, você é um bom herói :)')
                print('FIM')
        else:
            print('Sua cidade não está sendo atacada, parabéns :)')
            print('FIM')
    else:
        print('Você é um mau herói >:(')
        print('FIM')
