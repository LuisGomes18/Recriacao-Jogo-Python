import sys
import os
from random import randint


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extras.json_def import carregar_dados_player, guardar_dados_player
from extras.extra_def import pontuacao


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

    #NOTE: Modificar felicidade
    felicidade += int(inteligencia // 2)
    felicidade += int(amizade // 2)
    felicidade += int(criatividade // 2)

    dados['fase_crianca'][0]['inteligencia'] = inteligencia
    dados['fase_crianca'][0]['amizade'] = amizade
    dados['fase_crianca'][0]['criatividade'] = criatividade
    dados['recursos'][0]['felicidade'] = felicidade

    guardar_dados_player(dados)
    pontuacao()

    dados['fase_crianca'][0]['concluida'] = True
    guardar_dados_player(dados)
