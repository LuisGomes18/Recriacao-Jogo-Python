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


FASE_ADOLECENTE_TERMINADA = False
DEBUG = 0
VERDE = '\033[32m'
ORIGINAL= '\033[0;0m'

def fase_adolecente(vida, felicidade_atual): # pylint: disable=redefined-outer-name
    ''' Definicao da fase de adolecente '''
    atividades = int(input('''1) Artes
2) Medicina
3) Musica
4) Desporto
--> '''))
    while atividades not in [1,2,3,4]:
        atividades = int(input('''\n1) Artes
2) Medicina
3) Musica
4) Desporto
--> '''))

    dados_player["atividade_escolhida"] = atividades

    artes = randint(3, 9)
    medicina = randint(3, 9)
    musica = randint(3, 9)
    desporto = randint(3, 9)

    dados_player["artes"] = artes
    dados_player["medicina"] = medicina
    dados_player["musica"] = musica
    dados_player["desporto"] = desporto
    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)

    if atividades == 1 and artes == 9:
        print(f'{VERDE}Artes: {artes}{ORIGINAL}')
    elif artes != 9:
        print(f'Artes: {artes}')
    else:
        print('Valor incorreto')

    if atividades == 2 and medicina == 9:
        print(f'{VERDE}Medicina: {medicina}{ORIGINAL}')
    elif medicina != 9:
        print(f'Medicina: {medicina}')
    else:
        print('Valor incorreto')

    if atividades == 3 and musica == 9:
        print(f'{VERDE}Musica: {musica}{ORIGINAL}')
    elif musica != 9:
        print(f'Musica: {musica}')
    else:
        print('Valor incorreto')

    if atividades == 4 and desporto == 9:
        print(f'{VERDE}Desporto: {desporto}{ORIGINAL}')
    elif desporto != 9:
        print(f'Desporto: {desporto}')
    else:
        print('Valor incorreto')

    if atividades == 1:
        felicidade_atual += int(artes / 2)
    elif atividades == 2:
        felicidade_atual += int(medicina / 2)
    elif atividades == 3:
        felicidade_atual += int(musica / 2)
    elif atividades == 4:
        felicidade_atual += int(desporto / 2)
    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida)

    chances_amizade = []
    chance_amigo = randint(0, 100)
    if chance_amigo < 50:
        print('Você fez um novo amigo')
        felicidade_atual += 2
    else:
        print('Ele não quis ser teu amigo')
    chances_amizade.append(chance_amigo)

    chance_amigo_2 = randint(0, 100)
    if chance_amigo_2 < 50:
        print('Você fez um novo amigo')
        felicidade_atual += 2
    else:
        print('Ele não quis ser teu amigo')
    chances_amizade.append(chance_amigo_2)

    chance_amigo_3 = randint(0, 100)
    if chance_amigo_3 < 50:
        print('Você fez um novo amigo')
        felicidade_atual += 2
    else:
        print('Ele não quis ser teu amigo')
    chances_amizade.append(chance_amigo_3)

    dados_player['chance_amigo'] = chances_amizade

    # pylint: disable=invalid-name
    FASE_ADOLECENTE_TERMINADA = True # pylint: disable=redefined-outer-name
    dados_player['fase_adolecente_terminada'] = FASE_ADOLECENTE_TERMINADA
    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)

    return vida, felicidade_atual


if DEBUG == 1:
    with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
        conteudo_json = dados.read()
        dados_player = loads(conteudo_json)
    felicidade_atual = dados_player['felicidade']
    vida = dados_player['vida']
    vida, felicidade_atual = fase_adolecente(vida, felicidade_atual)
elif DEBUG == 0:
    pass
else:
    print('Valor Incorreto')
