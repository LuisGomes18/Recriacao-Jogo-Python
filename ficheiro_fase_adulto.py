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
#from extras import pontuacao
from extras import artes


FASE_ADULTO_TERMINADA = False
DEBUG = 1


def fase_adulto(vida, felicidade_atual): # pylint: disable=redefined-outer-name
    ''' Definicao da fase adulta'''
    atividade = dados_player['atividade_escolhida']
    if atividade == 1:
        nivel_atividade = dados_player['artes']
    elif atividade == 2:
        nivel_atividade = dados_player['medicina']
    elif atividade == 3:
        nivel_atividade = dados_player['musica']
    elif atividade == 4:
        nivel_atividade = dados_player['desporto']
    else:
        print('Valor invalido')
        exit(1)

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)

    if atividade == 1 and nivel_atividade == 9:
        artes(dados_player, felicidade_atual)
    # Moedas = 1->20$

    return vida, felicidade_atual

if DEBUG == 1:
    with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
        conteudo_json = dados.read()
        dados_player = loads(conteudo_json)
    felicidade_atual = dados_player['felicidade']
    vida = dados_player['vida']
    vida, felicidade_atual = fase_adulto(vida, felicidade_atual)
elif DEBUG == 0:
    pass
else:
    print('Valor Incorreto')
