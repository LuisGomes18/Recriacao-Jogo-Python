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
DEBUG = 1

def fase_adolecente(vida, felicidade_atual):
    ''' Definicao da fase de adolecente '''
    atividades = int(input('''1) Artes
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

    print(f'''
Artes: {artes}
Medicina: {medicina}
Música: {musica}
Desporto: {desporto}    
''')

    if atividades == 1:
        felicidade_atual += int(artes / 2)
    elif atividades == 2:
        felicidade_atual += int(medicina / 2)
    elif atividades == 3:
        felicidade_atual += int(musica / 2)
    elif atividades == 4:
        felicidade_atual += int(desporto / 2)
    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida)

    fumar = randint(3, 5)
    felicidade_atual -= int(fumar / 2)

    dados_player['felicidade'] = felicidade_atual
    dados_player['fumar'] = fumar

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida)

    # pylint: disable=invalid-name
    FASE_ADOLECENTE_TERMINADA = True
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
