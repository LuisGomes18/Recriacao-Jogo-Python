'''
Modulo para manusear ficheiros .json (l.5)
Modulo importar moduloda fase de bebe (l.6)
'''
from json import loads
from ficheiro_fase_bebe import fase_bebe

with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
    conteudo_json = dados.read()
    dados_player = loads(conteudo_json)

felicidade_atual = dados_player['felicidade']
vida = dados_player['vida']

if dados_player['fase_bebe_terminada'] == "true":
    felicidade_atual = fase_bebe(felicidade_atual)
elif dados_player['fase_bebe_terminada'] == "false":
    pass
