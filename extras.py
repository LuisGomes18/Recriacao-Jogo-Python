'''
JSON: Módulo utilizado para lidar com a serialização e desserialização de objetos JSON 
(JavaScript Object Notation). Ele fornece funções como loads para carregar ficheiros JSON 
com informações do jogo e dump para salvar as informações do Python em JSON num ficheiro.
'''
from json import loads, dump
from random import randint
import sys

AMARELO = '\033[33m'
ORIGINAL = '\033[0;0m'

with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
    conteudo_json = dados.read()
    dados_player = loads(conteudo_json)

vida = dados_player["vida"]
felicidade_atual = dados_player["felicidade"]

def pontuacao(felicidade_atual, vida):# pylint: disable=redefined-outer-name
    '''
    Mostra a pontuação atual do jogador.

    Parâmetros:
    felicidade_atual (int): A quantidade atual de felicidade do jogador.
    vida (int): A quantidade atual de vida do jogador.

    Esta função imprime a pontuação atual do jogador, incluindo a felicidade e a vida.
    Utiliza cores para destacar as informações na saída.
    '''
    print(AMARELO + f'\nFelicidade: {felicidade_atual}')
    print(f'Vida: {vida}\n' + ORIGINAL)


def artes(dados_player, felicidade_atual): # pylint: disable=redefined-outer-name
    """
    _summary_
    """
    moeda = randint(10, 80)
    dinheiro = moeda * 20
    dados_player['dinheiro'] = dinheiro

    with open("Data/Dados.json", 'w', encoding='utf-8') as dados: # pylint: disable=redefined-outer-name
        dump(dados_player, dados, ensure_ascii=False, indent=4)

    ajuda_1 = str(input('Quer ajudar sua colega: (S/N)\n-> ')) # type: ignore
    chance_ajuda_1 = randint(0, 100)
    if ajuda_1.lower() == "s" and chance_ajuda_1 > 50:
        print('Ela aceitou sua ajuda')
        felicidade_atual += 2
    elif ajuda_1.lower() == "n" and chance_ajuda_1 < 50:
        print('Ela não quis sua ajuda')
        felicidade_atual -= 2
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida)

    comida = randint(0, 6)
    fumar = randint(0 , 4)
    ginasio = randint(0, 4)

    ajuda_2 = str(input('Quer ir para a reunião (S/N)\n-> '))
    chance_reuniao = randint(0, 100)
    if ajuda_2.lower() == "s" and chance_reuniao < 30:
        print('Voçe foi na reunião e correu bem')
        felicidade_atual += 3
    elif ajuda_2.lower() == "s" and chance_reuniao > 30:
        print('Voce foi na reunião e correu mal')
        felicidade_atual -= 2
    elif ajuda_2.lower() == "n":
        print('Voce não foi a reunião')
        felicidade_atual -= 3
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida)

    felicidade_atual += int(comida / 3)
    felicidade_atual -= int(fumar / 3)
    dinheiro -= int(fumar / 2)
    felicidade_atual += int(ginasio / 3)
    # 3 AÇOES
