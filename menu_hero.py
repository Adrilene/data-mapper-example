from mapping import cidade_map, heroi_map, vilao_map
from domain import hero_domain


def heroi_menu():
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
            print(f'Sim, {vilao} está atacando.')
            escolha = input(f'Você deseja lutar ou fugir? (l/f)')
            while vilao.vida >= 0 and escolha == l:
                print('Status do vilão')
                print(f'Vilão: {vilao.nome}')
                print(f'Vida: {vilao.vida}')
                escolha = input(f'Você deseja lutar ou fugir? (l/f)')
            if escolha == 'f':
                print('Você é um mau herói >:(')
                print('FIM')
            else:
                print('Sua cidade está segura, parabéns, você é um bom herói :)')
                print('FIM')
        else: 
            print('Não, sua cidade está segura, parabéns :)')
            print('FIM')
    else: 
        print('Você é um mau herói >:(')
        print('FIM')