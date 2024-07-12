from random import randint
from extra import pontuacao
from json_def import carregar_dados_player, guardar_dados_player


def fase_crianca():
    print('''


███████╗ █████╗ ███████╗███████╗     ██████╗██████╗ ██╗ █████╗ ███╗   ██╗ ██████╗ █████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔══██╗██║██╔══██╗████╗  ██║██╔════╝██╔══██╗
█████╗  ███████║███████╗█████╗      ██║     ██████╔╝██║███████║██╔██╗ ██║██║     ███████║
██╔══╝  ██╔══██║╚════██║██╔══╝      ██║     ██╔══██╗██║██╔══██║██║╚██╗██║██║     ██╔══██║
██║     ██║  ██║███████║███████╗    ╚██████╗██║  ██║██║██║  ██║██║ ╚████║╚██████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝


''')

    dados = carregar_dados_player()

    felicidade = dados['recursos'][0]['felicidade']
    concluida = dados['fase_bebe'][0]['concluida']

    if not concluida:
        raise Exception('Fase bebe nao foi terminada')

    inteligencia = randint(0, 9)
    amizade = randint(0, 9)
    criatividade = randint(0, 9)

    if inteligencia >= 9:
        print(f'\033[32mInteligência: {inteligencia}\033[0m')
    else:
        print(f'Inteligência: {inteligencia}')

    if amizade >= 9:
        print(f'\033[32mAmizade: {amizade}\033[0m')
    else:
        print(f'Amizade: {amizade}')

    if criatividade >= 9:
        print(f'\033[32mCriatividade: {criatividade}\033[0m')
    else:
        print(f'Criatividade: {criatividade}')

    felicidade += int(inteligencia // 2) #! TMP
    felicidade += int(inteligencia // 2) #! TMP
    felicidade += int(inteligencia // 2) #! TMP

    dados['fase_crianca'][0]['inteligencia'] = inteligencia
    dados['fase_crianca'][0]['amizade'] = amizade
    dados['fase_crianca'][0]['criatividade'] = criatividade
    dados['recursos'][0]['felicidade'] = felicidade

    guardar_dados_player(dados)
    pontuacao()

    dados['fase_crianca'][0]['concluida'] = True
    guardar_dados_player(dados)
