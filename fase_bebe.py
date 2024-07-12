from random import randint
from extra import escolha_sexo, pontuacao
from json_def import carregar_dados_player, guardar_dados_player


def fase_bebe():
    print('''

    ███████╗ █████╗ ███████╗███████╗    ██████╗ ███████╗██████╗ ███████╗
    ██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔════╝
    █████╗  ███████║███████╗█████╗      ██████╔╝█████╗  ██████╔╝█████╗  
    ██╔══╝  ██╔══██║╚════██║██╔══╝      ██╔══██╗██╔══╝  ██╔══██╗██╔══╝  
    ██║     ██║  ██║███████║███████╗    ██████╔╝███████╗██████╔╝███████╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝╚═════╝ ╚══════╝

    ''')
    dados = carregar_dados_player()
    felicidade = dados['recursos'][0]['felicidade']

    concluida = dados['fase_crianca'][0]['concluida']
    if concluida:
        raise Exception('Config da fase criança precisa ser restaurado às definições de fábrica')

    escolha_sexo()

    pais = str(input('\nQuer ir com os pais (s/n)? ')).strip().lower()
    while pais not in ['s', 'n']:
        pais = str(input('Quer ir com os pais (s/n)? ')).strip().lower()

    if pais == 's':
        felicidade += 2
        print('Foste com os pais')
    elif pais == 'n':
        felicidade -= 2
        print('Foste sem os pais')

    dados['recursos'][0]['felicidade'] = felicidade
    dados['fase_crianca'][0]['pais'] = pais
    guardar_dados_player(dados)
    pontuacao()

    if pais == 's':
        biberao = randint(5, 9)
    else:
        biberao = randint(4, 9)

    felicidade += int(biberao //2)

    print(f'\nApanhas-te {biberao} biberoes\n')
    dados['fase_crianca'][0]['biberoes'] = biberao
    dados['recursos'][0]['felicidade'] = felicidade

    guardar_dados_player(dados) #! TMP
    pontuacao()

    escorrega = str(input('Quer ir ao escorrega (s/n)? ')).strip().lower()
    while escorrega not in ['s', 'n']:
        escorrega = str(input('Quer ir ao escorrega (s/n)? ')).strip().lower()

    if escorrega == 's':
        felicidade += 2
        print('Foste no escorrega')
    else:
        felicidade -= 2
        print('Não foste no escorrega')

    dados['recursos'][0]['felicidade'] = felicidade
    dados['fase_crianca'][0]['escorrega'] = escorrega
    guardar_dados_player(dados)
    pontuacao()

    dados['fase_crianca'][0]['concluida'] = True
    guardar_dados_player(dados)
