'''
JSON: Módulo utilizado para lidar com a serialização e desserialização de objetos JSON 
(JavaScript Object Notation). Ele fornece funções como loads para carregar ficheiros JSON 
com informações do jogo e dump para salvar as informações do Python em JSON num ficheiro.

Random: Módulo utilizado para gerar números pseudoaleatórios.
Ele fornece a função randint para gerar inteiros aleatórios dentro de um intervalo específico.

Extras: Um módulo personalizado que contém funções, uma delas é pontuacao.
'''
from json import loads
from json import dump
from random import randint
from extras import pontuacao


FASE_CRIANCA_TERMINADA = False
DEBUG = 0

def fase_crianca(dados_player, felicidade_atual, vida):
    ''' Definicao da fase de criança '''
    lampada = randint(1, 9)
    pintura = randint(1, 3)
    bebes = randint(1 , 3)
    media_felicidade = (lampada + pintura + bebes) // 3
    if lampada == 9:
        print('\033[32m' + f'Lampadas: {lampada}' + '\033[0m')
    else:
        print(f'Lampadas: {lampada}')
    if pintura == 3:
        print('\033[32m' + f'Pintar: {pintura}' + '\033[0m')
    else:
        print(f'Pintura: {pintura}')
    if bebes == 3:
        print('\033[32m' + f'Bebes: {bebes}' + '\033[0m')
    else:
        print(f'Bebes: {bebes}')
    dados_player["lampada"] = lampada
    dados_player["pintura"] = pintura
    dados_player["bebes"] = bebes

    felicidade_atual += media_felicidade
    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida)

    # pylint: disable=invalid-name
    FASE_CRIANCA_TERMINADA = True
    dados_player['fase_crianca_terminada'] = FASE_CRIANCA_TERMINADA
    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)

    return vida, felicidade_atual

if DEBUG == 1:
    with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
        conteudo_json = dados.read()
        dados_player = loads(conteudo_json)
    felicidade_atual = dados_player['felicidade']
    vida = dados_player['vida']
    vida, felicidade_atual = fase_crianca(dados_player, felicidade_atual, vida)
elif DEBUG == 0:
    pass
else:
    print('Valor Incorreto')
